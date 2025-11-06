# Política de Uso de Inteligencia Artificial Generativa

## Propósito
Establecer criterios éticos, académicos y técnicos para el uso de herramientas de Inteligencia Artificial Generativa (IAG) (p.ej. ChatGPT, Bard, Claude) en la elaboración de materiales y tareas del repositorio, garantizando transparencia, verificación y protección de datos.

## Principios
1. Apoyo, no sustitución: La IA se emplea como herramienta de apoyo (borradores, reestructuración, ideas) y nunca reemplaza análisis crítico, revisión disciplinar o juicio académico.
2. Transparencia: Todo documento asistido por IAG incluye una sección explícita "Transparencia sobre uso de IA" indicando alcance de la asistencia.
3. Verificación: Salidas se revisan manualmente para detectar errores factuales, sesgos, invenciones (alucinaciones) y se corrigen antes de aceptación final.
4. Respeto normativo: Para contenidos evaluables (PEC, TFG/TFM, pruebas), no se utiliza IA para generar texto salvo autorización explícita del equipo docente.
5. Privacidad y derechos: No se introducen datos personales, de terceros, ni material confidencial o protegido por copyright en prompts.
6. Citación: Contenido textual significativamente generado o inspirado por IAG se cita siguiendo guías (APA, MLA, Chicago, IEEE) cuando corresponda.
7. Trazabilidad: Prompts y versiones relevantes se registran en la carpeta `AI/prompts/`.

## Herramientas Cubiertas
- Modelos de texto: ChatGPT (GPT 3.5/4), Bard/Gemini, Claude.
- Modelos de apoyo estructural: Cualquier otro LLM usado para resumir, reordenar o proponer tablas.

## Procedimiento de Uso
1. Definir objetivo (ej.: resumir, mejorar estilo, generar tabla analítica) antes del prompt.
2. Redactar prompt responsable (ver guía de prompts) con: contexto, instrucción, restricciones, formato y criterios de calidad.
3. Registrar prompt en archivo `AI/prompts/<fecha>_<tema>.md` junto con salida inicial.
4. Revisar salida: comprobar referencias, datos numéricos, nombres propios, coherencia conceptual.
5. Documentar ajustes manuales: lista de correcciones aplicadas (factuales, estilísticas, estructurales).
6. Añadir al documento final el bloque de transparencia.

## Formato de Bloque de Transparencia (para insertar al final de cada documento)
```
## Transparencia sobre uso de IA
Este documento ha sido asistido por herramientas de Inteligencia Artificial Generativa en tareas de: <describir brevemente>. Todas las salidas fueron verificadas manualmente para corregir errores, alucinaciones y sesgos potenciales. No se introdujeron datos personales ni información confidencial. El contenido final refleja criterio académico propio.
```

## Informe de Uso (Plantilla)
```
Título / Documento:
Fecha:
Herramienta(s):
Versión (si conocida):
Objetivo del uso:
Prompts (enumeración):
Salida inicial (resumen):
Correcciones manuales aplicadas:
Verificación de referencias (resultado):
Evaluación de sesgos (checklist):
Decisión final / Observaciones:
Revisor responsable:
```

## Checklist de Verificación Rápida
| Ítem | Sí/No | Observaciones |
|------|-------|---------------|
| Datos numéricos verificados |  |  |
| Referencias existentes (DOI / fuente) |  |  |
| Ausencia de alucinaciones (personas/leyes inventadas) |  |  |
| Neutralidad cultural / género |  |  |
| Tono académico apropiado |  |  |
| Estructura lógica y coherente |  |  |
| Correspondencia con fuentes internas (apuntes, guías) |  |  |

## Citación de Contenido Generado
Ejemplo APA (adaptado de directrices APA para ChatGPT):
> OpenAI. (2025). Respuesta de ChatGPT a prompt sobre formación de orientadores [Comunicación generada]. https://chat.openai.com/

Incluir en cuerpo: "(Contenido asistido por ChatGPT, ver sección de transparencia)."

## Gestión de Sesgos
- Revisar lenguaje para evitar estereotipos.
- Contrastar afirmaciones sobre colectivos con fuentes oficiales.
- Ajustar términos a diversidad e inclusión (p.ej. "alumnado con necesidades específicas de apoyo educativo").

## Limitaciones Aceptadas
- La IA puede producir errores factuales y referencias falsas.
- No se consideran originales las ideas generadas sin reelaboración crítica.
- Instrumento estadístico sin comprensión semántica real.

## Política de Commits
- Prefijo `ai:` en mensajes de commit cuando el cambio principal incorpora asistencia de IA (ej.: `ai(docs): reestructura síntesis Debate 3`).
- Prefijo `docs:` para documentación sin asistencia.

## Privacidad
No introducir: nombres completos de terceros, datos personales (email, teléfono), identificadores sensibles, fragmentos extensos de textos protegidos.

## Revisión Periódica
Actualizar este documento trimestralmente o cuando cambien herramientas/políticas institucionales.

## Referencias Técnicas
- UNED (2023). Guía de uso de herramientas de Inteligencia Artificial Generativa para el estudiantado.
- APA Style Blog: How to cite ChatGPT.
- MLA Style Center: Citing Generative AI.
- Chicago Manual of Style: Guidance on AI-generated text.

---
Versión 1.0 – 2025-11-06
