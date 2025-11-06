#!/usr/bin/env python3
"""
Generador de Informe de Uso de IA
---------------------------------
Reúne información de registros de prompts en AI/prompts/ y produce un
informe Markdown siguiendo la plantilla `INFORME_USO_TEMPLATE.md`.

Uso:
  python generar_informe_uso.py \
    --prompts-dir AI/prompts \
    --output informe_uso_debate3.md \
    --documento "Debate 3" \
    --ruta "Primer cuatrimestre/Politicas y sistemas/Foros/Debate 3/Debate3.md" \
    --herramientas "ChatGPT GPT-4" \
    --objetivo "Reestructurar debate (síntesis, tabla, hilos, conclusión)"

Argumentos opcionales adicionales:
  --fecha YYYY-MM-DD (por defecto fecha actual)
  --autor "Nombre Revisor"

El script intenta extraer para cada prompt:
  Número, texto del prompt, motivo (heurística a partir del título),
  observaciones/correcciones breves.

Limitaciones:
  - Supone formato similar al ejemplo `debate3_2025-11-06.md`.
  - Si no puede parsear algún segmento, lo marca con `[no extraído]`.

Salida:
  Archivo Markdown listo para revisión manual final.
"""
from __future__ import annotations
import argparse
import datetime as _dt
import pathlib
import re
import sys
from typing import List, Dict, Any, Tuple

PROMPT_SECTION_RE = re.compile(r'^## Prompt (\d+) \(([^)]+)\)', re.MULTILINE)
CODE_BLOCK_RE = re.compile(r'```[\s\S]*?```', re.MULTILINE)
CORRECCIONES_RE = re.compile(r'^Correcciones manuales?:\s*(.*)$', re.MULTILINE)
SALIDA_RE = re.compile(r'^Salida inicial(?: \(extracto\))?:\s*(.*)$', re.MULTILINE)
EVAL_SESGOS_RE = re.compile(r'^## Evaluación de Sesgos\n(?P<body>(?:^- .+\n?)+)', re.MULTILINE)
VERIF_FACTUAL_RE = re.compile(r'^## Verificación Factual\n(?P<body>(?:^- .+\n?)+)', re.MULTILINE)

def parse_prompt_file(path: pathlib.Path) -> Tuple[List[Dict[str, Any]], Dict[str, List[str]]]:
    text = path.read_text(encoding='utf-8', errors='replace')
    prompts = []
    for m in PROMPT_SECTION_RE.finditer(text):
        numero = m.group(1)
        motivo = m.group(2).strip()
        # Slice from this match to next or end
        start = m.end()
        next_matches = [nm for nm in PROMPT_SECTION_RE.finditer(text, start)]
        end = next_matches[0].start() if next_matches else len(text)
        segment = text[start:end]
        # Extract first code block as prompt text
        code_match = CODE_BLOCK_RE.search(segment)
        prompt_text = code_match.group(0).strip('`') if code_match else '[no extraído]'
        salida_match = SALIDA_RE.search(segment)
        salida = salida_match.group(1).strip() if salida_match else '[no extraído]'
        corr_match = CORRECCIONES_RE.search(segment)
        correcciones = corr_match.group(1).strip() if corr_match else '[no extraído]'
        prompts.append({
            'numero': numero,
            'motivo': motivo,
            'prompt': sanitize_inline(prompt_text),
            'salida': salida,
            'correcciones': correcciones,
            'fuente_archivo': path.name
        })
    # Extra sections (global at file level) - evaluation and factual verification
    sesgos_lines: List[str] = []
    factual_lines: List[str] = []
    sesgos_match = EVAL_SESGOS_RE.search(text)
    if sesgos_match:
        sesgos_lines = [ln[2:].strip() for ln in sesgos_match.group('body').splitlines() if ln.startswith('- ')]
    factual_match = VERIF_FACTUAL_RE.search(text)
    if factual_match:
        factual_lines = [ln[2:].strip() for ln in factual_match.group('body').splitlines() if ln.startswith('- ')]
    return prompts, {'sesgos': sesgos_lines, 'factual': factual_lines}

INLINE_NEWLINE_RE = re.compile(r'\s*\n\s*')

def sanitize_inline(s: str) -> str:
    # Collapse whitespace and limit length
    s = INLINE_NEWLINE_RE.sub(' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s[:250] + ('…' if len(s) > 250 else '')

def build_prompts_table(prompts: List[Dict[str, Any]]) -> str:
    if not prompts:
        return '| Nº | Prompt | Motivo | Observaciones de salida |\n|----|--------|--------|-------------------------|\n| 1 | (sin registros) | - | - |'
    rows = ['| Nº | Prompt | Motivo | Observaciones de salida |', '|----|--------|--------|-------------------------|']
    for p in prompts:
        obs = p['correcciones'] if len(p['correcciones']) < 90 else p['correcciones'][:87] + '…'
        rows.append(f"| {p['numero']} | {escape_pipe(p['prompt'])} | {escape_pipe(p['motivo'])} | {escape_pipe(obs)} |")
    return '\n'.join(rows)

def escape_pipe(s: str) -> str:
    return s.replace('|', '¦')

def clamp_words(text: str, max_words: int) -> str:
    words = text.split()
    if len(words) <= max_words:
        return text
    return ' '.join(words[:max_words]) + '…'

def generate_report(args: argparse.Namespace, prompts: List[Dict[str, Any]],
                    extra: Dict[str, List[str]], checklist_block: str | None) -> str:
    fecha = args.fecha or _dt.date.today().isoformat()
    # Auto resumen (primer prompt salida si existe)
    resumen = '> (Completar con extracto ≤120 palabras representativo de la primera respuesta global)'
    if prompts:
        salida0 = prompts[0].get('salida', '').strip()
        if salida0 and salida0 != '[no extraído]':
            resumen_text = clamp_words(salida0, args.max_resumen_palabras)
            resumen = '> ' + resumen_text

    factual_prev = ''
    if extra.get('factual'):
        factual_prev = '**Extracto verificación factual (origen registro prompts):**\n' + '\n'.join(f'- {ln}' for ln in extra['factual']) + '\n'

    sesgos_prev = ''
    if extra.get('sesgos'):
        sesgos_prev = '**Extracto evaluación de sesgos (registro prompts):**\n' + '\n'.join(f'- {ln}' for ln in extra['sesgos']) + '\n'

    checklist_section: List[str] = []
    if checklist_block:
        checklist_section = ['','## Checklist (Plantilla Referencial)','(Copiada de `AI/CHECKLIST_SESGOS.md` – completar en caso necesario)','', checklist_block]

    header = [
        '# Informe de Uso de IA',
        '',
        '## Metadatos',
        f'- Documento / Tarea: {args.documento}',
        f'- Ruta en repo: {args.ruta}',
        f'- Fecha: {fecha}',
        f'- Autor responsable revisión: {args.autor}',
        f'- Herramienta(s) IA utilizadas (modelo y versión si aplica): {args.herramientas}',
        '',
        '## Objetivo del Uso',
        args.objetivo,
        '',
        '## Prompts Utilizados',
        build_prompts_table(prompts),
        '',
        '## Salida Inicial (Resumen)',
        resumen,
        '',
        '## Correcciones Manuales Aplicadas',
        '1. (Completar lista)',
        '',
        '## Verificación Factual',
        factual_prev,
        '| Ítem | Resultado | Fuente confirmación |',
        '|------|-----------|---------------------|',
        '| Datos numéricos (ratios, fechas) |  |  |',
        '| Referencias bibliográficas |  |  |',
        '| Entidades / nombres propios |  |  |',
        '| Conceptos clave definidos |  |  |',
        '',
        '## Evaluación de Sesgos / Calidad',
        sesgos_prev,
        '| Criterio | OK | Observaciones |',
        '|----------|----|--------------|',
        '| Neutralidad cultural/género |  |  |',
        '| Lenguaje inclusivo |  |  |',
        '| Ausencia de estereotipos |  |  |',
        '| Tono académico adecuado |  |  |',
        '| Coherencia estructural |  |  |',
        '| Transparencia (sección añadida) |  |  |',
        '',
        '## Riesgos Detectados y Mitigación',
        '| Riesgo | Acción de mitigación | Estado |',
        '|--------|----------------------|--------|',
        '| Referencias inventadas | Verificar DOIs |  |',
        '| Información desactualizada | Contrastar normativa vigente |  |',
        '| Ambigüedad conceptual | Definir términos en glosario |  |',
        '',
        '## Decisión Final',
        '(Completar: aceptado / parcial / descartado, justificar)',
        '',
        '## Comentarios Adicionales',
        'Indicaciones sobre mejoras futuras de prompting.'
    ] + checklist_section + [
        '',
        '---',
        f'Generado automáticamente {fecha} por generar_informe_uso.py (revisión manual requerida)'
    ]
    return '\n'.join([part for part in header if part is not None])
    return '\n'.join(header)

def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(description='Genera informe de uso de IA desde registros de prompts.')
    parser.add_argument('--prompts-dir', default='AI/prompts', help='Directorio con archivos de registro de prompts (.md)')
    parser.add_argument('--output', required=True, help='Ruta del archivo Markdown de salida')
    parser.add_argument('--documento', required=True, help='Nombre documento/tarea')
    parser.add_argument('--ruta', required=True, help='Ruta relativa en el repositorio')
    parser.add_argument('--herramientas', default='(especificar)', help='Herramientas IA usadas')
    parser.add_argument('--objetivo', required=True, help='Objetivo del uso de IA')
    parser.add_argument('--fecha', help='Fecha ISO (YYYY-MM-DD)')
    parser.add_argument('--autor', default='(revisor)', help='Autor responsable de la revisión')
    parser.add_argument('--max-resumen-palabras', type=int, default=120, help='Límite de palabras para el resumen inicial automático')
    parser.add_argument('--incluir-checklist', action='store_true', help='Incluye la tabla base de la checklist de sesgos')
    args = parser.parse_args(argv)

    prompts_dir = pathlib.Path(args.prompts_dir)
    if not prompts_dir.exists():
        print(f'Directorio de prompts no encontrado: {prompts_dir}', file=sys.stderr)
        return 2

    prompt_files = sorted(prompts_dir.glob('*.md'))
    all_prompts: List[Dict[str, Any]] = []
    extra_global: Dict[str, List[str]] = {'sesgos': [], 'factual': []}
    for pf in prompt_files:
        try:
            parsed, extra = parse_prompt_file(pf)
            all_prompts.extend(parsed)
            # merge extra lines (avoid duplicates)
            for k in extra_global.keys():
                for line in extra.get(k, []):
                    if line not in extra_global[k]:
                        extra_global[k].append(line)
        except Exception as e:
            print(f'Error procesando {pf.name}: {e}', file=sys.stderr)

    checklist_block = None
    if args.incluir_checklist:
        checklist_path = pathlib.Path('AI/CHECKLIST_SESGOS.md')
        if checklist_path.exists():
            try:
                ctext = checklist_path.read_text(encoding='utf-8', errors='replace')
                # Extract first table only (until blank line after header separator)
                lines = ctext.splitlines()
                table_lines = []
                in_table = False
                for ln in lines:
                    if ln.startswith('| Categoría'):
                        in_table = True
                    if in_table:
                        if ln.strip() == '' and table_lines:
                            break
                        table_lines.append(ln)
                if table_lines:
                    checklist_block = '\n'.join(table_lines)
            except Exception as e:
                print(f'No se pudo leer checklist: {e}', file=sys.stderr)

    report = generate_report(args, all_prompts, extra_global, checklist_block)
    out_path = pathlib.Path(args.output)
    out_path.write_text(report, encoding='utf-8')
    print(f'Informe generado: {out_path} (prompts procesados: {len(all_prompts)})')
    return 0

if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
