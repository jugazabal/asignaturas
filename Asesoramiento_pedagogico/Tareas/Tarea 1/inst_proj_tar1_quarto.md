<!-- cSpell:language es,es-ES -->

# PROYECTO QUARTO PARA TAREA 1: FICHAS RESUMEN DE ENFOQUES TEÓRICOS

## 📋 Guía para crear un documento académico en formato APA usando Quarto

Esta guía te ayudará a configurar un proyecto Quarto que cumple con las **normas APA** para la Tarea 1 de Asesoramiento Psicopedagógico, con capacidad de exportar a **PDF** y **HTML**.

---

## 🔧 REQUISITOS PREVIOS

Antes de comenzar, asegúrate de tener instalado:

- ✅ **Quarto CLI**: https://quarto.org/docs/get-started/
- ✅ **Distribución LaTeX** (para renderizar PDF):
  - TinyTeX (recomendado): Ejecutar `quarto install tinytex` en terminal
  - O TeX Live completo
- ⚠️ **Consulta**: `apa_guidelines.md` para detalles completos del formato APA

---

## 📁 ESTRUCTURA DEL PROYECTO

Crea una carpeta para tu tarea con la siguiente estructura:

```
Tarea_1_Enfoques_Teoricos/
├── tarea1.qmd                 # Documento principal
├── _quarto.yml                # Configuración del proyecto
├── apa.csl                    # Archivo de estilo APA
├── references.bib             # Bibliografía
└── apa_guidelines.md          # Guía de referencia APA
```

---

## 📝 ARCHIVO PRINCIPAL: `tarea1.qmd`

### Configuración del encabezado (YAML frontmatter)

```yaml
---
title: "Fichas Resumen de los Enfoques Teóricos de Asesoramiento Psicopedagógico"
subtitle: "Tarea 1 - Asesoramiento Psicopedagógico"
author: 
  - name: "Tu Nombre Completo"
    affiliation: "UNED - Máster en Formación del Profesorado"
date: today
date-format: "D [de] MMMM [de] YYYY"
lang: es
format:
  html:
    theme: cosmo
    toc: true
    toc-depth: 3
    toc-title: "Índice"
    code-fold: true
    number-sections: true
    css: styles.css
  pdf:
    documentclass: article
    papersize: a4
    fontsize: 12pt
    geometry: 
      - margin=2.5cm
    linestretch: 1.5
    cite-method: biblatex
    keep-tex: true
    number-sections: true
    toc: false
bibliography: references.bib
csl: apa.csl
---
```

### Estructura del contenido (según normas APA y UNED)

```markdown
# Resumen {.unnumbered}

::: {.callout-note}
**Extensión recomendada**: 150-250 palabras (según `apa_guidelines.md`)
:::

Resumen conciso de las perspectivas teóricas analizadas, metodología empleada, 
principales hallazgos y conclusiones del trabajo.

**Palabras clave**: Asesoramiento psicopedagógico, perspectivas teóricas, 
orientación educativa, enfoques de intervención.

{{< pagebreak >}}

# Introducción

## Planteamiento del trabajo

[Introducción al tema del asesoramiento psicopedagógico y justificación del 
análisis de las diferentes perspectivas teóricas]

## Objetivos

El presente trabajo tiene como objetivos:

1. Comprender las principales perspectivas teóricas del asesoramiento psicopedagógico
2. Identificar y describir los enfoques derivados de cada perspectiva
3. Analizar críticamente las ventajas y limitaciones de cada enfoque
4. Reflexionar sobre su aplicabilidad en contextos educativos reales

{{< pagebreak >}}

# Perspectivas Teóricas del Asesoramiento Psicopedagógico

## Perspectiva Social

### Enfoque 1: [Nombre del enfoque]

#### Autores principales
[@apellido2020; @apellido2019]

#### Principios teóricos fundamentales
[Descripción de los fundamentos teóricos...]

#### Objetivos del asesoramiento
[Finalidades específicas de este enfoque...]

#### Rol del asesor psicopedagógico
[Funciones y actuaciones del asesor...]

#### Ventajas del enfoque
- Ventaja 1
- Ventaja 2

#### Limitaciones del enfoque
- Limitación 1
- Limitación 2

#### Valoración crítica personal
[Análisis reflexivo propio sobre el enfoque, con ejemplos contextualizados 
en el ámbito educativo español...]

---

### Enfoque 2: [Si existe otro enfoque dentro de la perspectiva social]

[Repetir estructura anterior]

---

## Perspectiva Pedagógica

[Seguir la misma estructura de apartados]

---

## Perspectiva Psicológica

[Incluir sus diferentes enfoques si los hubiere]

---

## Perspectiva Psicopedagógica

[Seguir la estructura completa]

{{< pagebreak >}}

# Análisis Comparativo

## Cuadro resumen de perspectivas

| Perspectiva | Enfoque principal | Rol del asesor | Principales autores |
|-------------|-------------------|----------------|---------------------|
| Social      | ...              | ...            | ...                 |
| Pedagógica  | ...              | ...            | ...                 |
| Psicológica | ...              | ...            | ...                 |
| Psicopedagógica | ...          | ...            | ...                 |

: Comparativa de las perspectivas teóricas del asesoramiento {#tbl-comparativa}

---

# Conclusiones

## Síntesis de hallazgos principales

[Resumen de los aspectos clave de cada perspectiva...]

## Reflexión final

[Valoración personal sobre la importancia de conocer las diferentes 
perspectivas para la práctica profesional...]

## Aplicabilidad práctica

[Cómo estos enfoques pueden aplicarse en contextos educativos reales...]

{{< pagebreak >}}

# Referencias {.unnumbered}

::: {#refs}
:::
```

---

## ⚙️ ARCHIVO DE CONFIGURACIÓN: `_quarto.yml`

```yaml
project:
  type: manuscript
  output-dir: _output

lang: es

format:
  html:
    theme: cosmo
    toc: true
    toc-depth: 3
    number-sections: true
    smooth-scroll: true
    highlight-style: github
  pdf:
    documentclass: article
    papersize: a4
    fontsize: 12pt
    geometry:
      - margin=2.5cm
    linestretch: 1.5
    cite-method: biblatex
    keep-tex: true
    number-sections: true
    colorlinks: true

bibliography: references.bib
csl: apa.csl
```

---

## 📚 ARCHIVO DE BIBLIOGRAFÍA: `references.bib`

Crea un archivo `references.bib` con tus fuentes en formato BibTeX:

```bibtex
@book{autor2020,
  author = {Apellido, Nombre},
  title = {Título del libro sobre asesoramiento psicopedagógico},
  publisher = {Editorial},
  year = {2020},
  address = {Ciudad}
}

@article{autor2019,
  author = {Apellido, Nombre and Apellido2, Nombre2},
  title = {Título del artículo sobre perspectivas teóricas},
  journal = {Revista de Orientación Educativa},
  volume = {15},
  number = {2},
  pages = {123--145},
  year = {2019}
}

@incollection{autor2018,
  author = {Apellido, Nombre},
  title = {Capítulo sobre enfoques de asesoramiento},
  booktitle = {Manual de orientación educativa},
  editor = {Editor, Nombre},
  publisher = {Editorial Universitaria},
  year = {2018},
  pages = {45--67}
}
```

---

## 🎨 ARCHIVO CSL: `apa.csl`

Descarga el archivo de estilo APA desde:
- **Repositorio Zotero**: https://www.zotero.org/styles/apa
- Guarda el archivo como `apa.csl` en la carpeta del proyecto

---

## 📐 CUMPLIMIENTO DE NORMAS APA Y UNED

### Según `apa_guidelines.md`:

#### ✅ Formato del documento (PDF)
- **Fuente**: 12pt (configurado en YAML: `fontsize: 12pt`)
- **Interlineado**: 1.5 (configurado: `linestretch: 1.5`)
- **Márgenes**: 2.5 cm (configurado: `geometry: margin=2.5cm`)
- **Extensión**: Máximo 6 páginas (controlar manualmente)

#### ✅ Estructura requerida
1. **Portada** con datos del estudiante ✓
2. **Resumen/Abstract** (150-250 palabras) ✓
3. **Introducción** con objetivos ✓
4. **Cuerpo principal** con las 4 perspectivas ✓
5. **Conclusiones** ✓
6. **Referencias** (no cuentan en las 6 páginas) ✓

#### ✅ Estilo de escritura (APA)
- Escribir en **tercera persona** (evitar "yo", "nosotros")
- Usar **lenguaje académico** formal
- **Citar correctamente** usando formato APA: `[@autor2020]` o `@autor2020`
- **No usar contracciones** (usar "no es" en lugar de "no's")
- **Evitar preposiciones** al final de las oraciones

#### ✅ Citas y referencias
- **Citas en texto APA**: 
  - Una fuente: `[@apellido2020]` → (Apellido, 2020)
  - Múltiples fuentes: `[@apellido2020; @apellido2019]` → (Apellido, 2020; Apellido, 2019)
  - Cita narrativa: `@apellido2020` → Apellido (2020)
- **Lista de referencias**: Generada automáticamente al final

---

## 🚀 RENDERIZAR EL PROYECTO

### Para generar ambos formatos (PDF + HTML):

```bash
quarto render tarea1.qmd
```

### Solo PDF:

```bash
quarto render tarea1.qmd --to pdf
```

### Solo HTML:

```bash
quarto render tarea1.qmd --to html
```

### Vista previa interactiva:

```bash
quarto preview tarea1.qmd
```

---

## 📊 RESULTADO FINAL

El proceso generará:

- **`tarea1.pdf`**: Documento formateado según normas APA para entregar en la UNED
- **`tarea1.html`**: Versión web para consulta personal
- **`tarea1.tex`**: Archivo LaTeX intermedio (si necesitas ajustes avanzados)

---

## ✅ CHECKLIST ANTES DE ENTREGAR

Revisa que tu documento cumple:

### Formato y estructura
- [ ] Extensión máxima de 6 páginas (sin contar referencias)
- [ ] Fuente 12pt, márgenes 2.5cm, interlineado 1.5
- [ ] Incluye portada con datos del estudiante
- [ ] Incluye resumen/abstract de 150-250 palabras
- [ ] Estructura clara: Introducción → Perspectivas → Conclusiones → Referencias

### Contenido académico
- [ ] Las 4 perspectivas están completas (Social, Pedagógica, Psicológica, Psicopedagógica)
- [ ] Cada perspectiva tiene los 7 apartados obligatorios
- [ ] Incluye ejemplos educativos contextualizados
- [ ] Valoración crítica personal en cada enfoque
- [ ] Lenguaje académico en tercera persona

### Citas y referencias
- [ ] Todas las afirmaciones importantes están citadas
- [ ] Las citas siguen formato APA
- [ ] La lista de referencias está completa y correcta
- [ ] Mínimo 7 fuentes, máximo 11 (según guía APA)
- [ ] No se usa excesivamente una sola fuente

### Calidad
- [ ] Revisión ortográfica completada
- [ ] Revisión de estilo académico
- [ ] Sin plagio (trabajo original)
- [ ] Archivo en formato PDF para entrega

---

## 💡 CONSEJOS ADICIONALES

### Para trabajar eficientemente con Quarto:

1. **Usa Visual Studio Code** con la extensión de Quarto
2. **Vista previa en tiempo real**: `quarto preview` mientras escribes
3. **Control de versiones**: Usa Git para guardar progreso
4. **Gestión de citas**: Usa Zotero o Mendeley y exporta a BibTeX
5. **Revisar PDF frecuentemente**: Asegúrate de que no excedes 6 páginas

### Para cumplir con APA:

- **Consulta `apa_guidelines.md`** regularmente durante la escritura
- **Ejemplos de citas**:
  - Parafraseo: "Según López (2020), el asesoramiento psicopedagógico..."
  - Cita textual corta: "El asesoramiento es un proceso colaborativo" (García, 2019, p. 45)
  - Cita textual larga (>40 palabras): Usar bloque indentado
- **Referencias**: Verifica que cada cita en texto tenga su referencia completa

---

## 📖 RECURSOS ADICIONALES

- **Guía APA completa**: Ver `apa_guidelines.md` en esta carpeta
- **Purdue OWL APA Guide**: https://owl.purdue.edu/owl/research_and_citation/apa_style/
- **Quarto Documentation**: https://quarto.org/docs/guide/
- **Quarto APA Format**: https://quarto.org/docs/extensions/formats.html

---

**Fecha de actualización**: 24 de octubre de 2025

**Nota importante**: Este archivo debe usarse junto con `apa_guidelines.md` para asegurar el cumplimiento completo de las normas APA y los requisitos específicos de la UNED para la Tarea 1.
