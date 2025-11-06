# Guía de Diseño de Prompts Responsables

## Objetivo
Optimizar la calidad y fiabilidad de las respuestas de herramientas de Inteligencia Artificial Generativa (IAG) asegurando contexto suficiente, restricciones claras y formato verificable.

## Componentes Clave de un Prompt
1. Contexto / Rol
   - Indica a la IA quién debe "ser" o el marco de actuación.
   - Ejemplo: "Actúa como un orientador educativo especializado en formación inicial de orientadores en España".
2. Objetivo
   - Qué necesitas exactamente (resumir, comparar, generar casos, estructurar tabla, cuestionario, etc.).
3. Contenido fuente / Datos
   - Proporciona los fragmentos relevantes (apuntes, citas breves). Evita pegar textos confidenciales.
4. Restricciones
   - Idioma, extensión (número de palabras/párrafos), formato (Markdown, tabla), tono (académico, divulgativo), nivel (grado/máster).
5. Formato de salida
   - Plantilla esperada o ejemplo de estructura.
6. Criterios de calidad / Verificación solicitada
   - Pide marcar incertidumbres, citar fuentes plausibles, evitar inventar referencias.
7. Iteración
   - Si respuesta no cumple, refinar con un segundo prompt indicando ajustes.

## Plantilla General
```
Contexto/Rol: <definir>
Objetivo: <definir>
Fuente/Base: <apuntes/resumen breve>
Restricciones: idioma=es, extensión=<x> palabras, tono=académico, formato=Markdown
Formato salida: <ejemplo o estructura>
Verificación: Indica dudas, NO inventes referencias; si algo no es seguro, márcalo como "[incertidumbre]".
```

## Ejemplo Completo
```
Actúa como un experto en orientación educativa europea.
Necesito una tabla comparativa de 5 columnas que contraste: (1) perfil del orientador, (2) formación inicial, (3) especialización, (4) ratio habitual, (5) retos.
Usa estas notas: "España: máster habilitante; ratios altas; diversidad competencial. EEUU: rol heterogéneo; tareas administrativas. Finlandia: universalidad, continuidad".
Restricciones: idioma=es, máximo=180 palabras totales, formato=Markdown.
Formato salida: | País | Perfil | Formación | Ratio | Retos |
Verificación: Si falta dato pon "[dato no disponible]" sin inventar.
```

## Lista de Verificación Pre-Prompt
| Ítem | OK | Nota |
|------|----|------|
| Objetivo es específico |  |  |
| Texto fuente resumido |  |  |
| No incluye datos personales |  |  |
| Se definieron restricciones |  |  |
| Formato de salida claro |  |  |
| Se pidió marcar incertidumbre |  |  |

## Buenas Prácticas
- Empezar simple, luego refinar (iteración).
- Descomponer tareas complejas: primero esquema, luego ampliar secciones.
- Evitar prompts vagos como "Explícame todo sobre...".
- Usar delimitadores para contenido fuente: ```APUNTES ... ``` para reducir confusión.
- Pedir opciones comparativas: "Genera 3 versiones con distinta densidad".

## Errores Comunes
| Error | Consecuencia | Corrección |
|-------|--------------|------------|
| Falta de restricciones | Respuestas extensas o irrelevantes | Añadir límites de longitud y formato |
| Objetivo múltiple mezclado | Salida confusa | Dividir en prompts separados |
| Solicitar referencias sin control | Riesgo de inventadas | Pedir marcar fuentes dudosas y luego validar manualmente |
| Insertar datos sensibles | Riesgo privacidad | Anonimizar o no incluir |

## Indicadores de Calidad de Respuesta
- Cobertura: ¿Responde todos los elementos del objetivo?
- Precisión: ¿Evita afirmaciones sin soporte?
- Claridad: ¿Estructura y formato según especificado?
- Marcado de incertidumbre: ¿Señala lo que no puede asegurar?
- Ausencia de alucinaciones evidentes: No referencias fabricadas.

## Refinamiento (Prompt de Corrección)
Ejemplo de prompt de segunda iteración:
```
Anterior respuesta: <resumen breve>
Correcciones: Añade columna "Fuentes", reduce a 120 palabras, marca datos dudosos.
Repite solo la tabla final.
```

## Seguridad y Privacidad
- Nunca incluir nombres completos, emails, datos de terceros.
- No pegar fragmentos extensos de textos con copyright no autorizados.

## Control de Sesgos
Instrucción adicional sugerida:
```
Revisa la salida para evitar sesgos culturales y de género; usa lenguaje inclusivo y neutral.
```

## Ejemplos Rápidos de Prompt por Tarea
| Tarea | Prompt base |
|-------|-------------|
| Resumen | "Resume en 120 palabras el siguiente texto delimitado, manteniendo conceptos clave y marcando datos inciertos con [?]: ```TEXTO```" |
| Mejora estilo | "Mejora claridad y cohesión del texto, sin añadir ideas nuevas, señalando frases ambiguas: ```TEXTO```" |
| Flashcards | "Genera 10 flashcards (Formato: Term|Definición corta) de estos conceptos: A, B, C. Indica si algún término carece de definición clara." |
| Tabla comparativa | "Crea tabla Markdown de X vs Y vs Z con columnas Perfil/Formación/Reto, usando notas: ```NOTAS```; si falta dato escribe [no disponible]." |
| Autoevaluación | "Genera 8 preguntas tipo test sobre estos apuntes: ```APUNTES```. 4 opciones cada una, marca la correcta y una justificación breve." |

## Registro
Tras usar un prompt, registrar en `prompts/<fecha>_<tema>.md`:
- Prompt final
- Herramienta y versión (si conocida)
- Salida inicial (recortada)
- Ajustes realizados

## Actualización
Revisar esta guía cada 6 meses o tras cambios tecnológicos significativos.

---
Versión 1.0 – 2025-11-06
