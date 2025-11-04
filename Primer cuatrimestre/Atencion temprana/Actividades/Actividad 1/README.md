# Actividad 1 - Atención Temprana y Orientación Familiar

## Descripción

Este proyecto Quarto contiene la respuesta a la Actividad 1 de la asignatura Atención Temprana y Orientación Familiar del Máster en Formación del Profesorado (UNED).

**Pregunta central**: ¿Qué papel podría desempeñar la familia en la Atención Temprana? ¿Qué es la AT centrada en la Familia?

## Estructura del Proyecto

```
Actividad 1/
├── actividad1.qmd          # Documento principal Quarto
├── actividad1.md           # Instrucciones de la actividad
├── _quarto.yml             # Configuración Quarto
├── references.bib          # Referencias bibliográficas
├── apa.csl                 # Estilo de citación APA 7
├── README.md               # Este archivo
├── .gitignore              # Archivos excluidos de Git
└── Bibliografia Tema 1 txt/ # Textos fuente convertidos de PDF
    ├── 2025_ConsensoAT.txt
    ├── art_FAlberto_Garcia_Schz_Atencion-temprana-centrada-en-la-familia.txt
    ├── Guia_Basica_AT_Transformacion_atencion_temprana_bbppinteractivo.txt
    ├── Hoja de Ruta_BOE-A-2025-4747.txt
    └── Informe-de-la-situacion-de-la-Atencion-temprana-2024.txt
```

## Compilación

### Generar PDF

```bash
quarto render actividad1.qmd --to pdf
```

### Generar HTML

```bash
quarto render actividad1.qmd --to html
```

### Generar ambos formatos

```bash
quarto render actividad1.qmd
```

### Vista previa interactiva

```bash
quarto preview actividad1.qmd
```

## Requisitos

- Quarto 1.3 o superior
- LaTeX (TinyTeX recomendado para PDF)
- Pandoc (incluido con Quarto)

### Instalación de TinyTeX

```bash
quarto install tinytex
```

## Contenido del Documento

El documento `actividad1.qmd` desarrolla los siguientes apartados:

1. **Introducción**: Contextualización de la pregunta sobre el papel de la familia en AT
2. **El Papel de la Familia en la Atención Temprana**:
   - Evolución histórica del rol familiar
   - La familia como elemento multidimensional (cliente, responsable legal, recurso, agente activo)
   - Fundamentos neuropsicológicos del papel familiar
3. **La Atención Temprana Centrada en la Familia**:
   - Definición y características
   - Principios fundamentales
   - Diferencias con el modelo ambulatorio tradicional
   - Marco normativo y recomendaciones
   - Estrategias de implementación
   - Beneficios documentados
   - Retos y necesidades de transformación
4. **Valoración Crítica Personal**: Reflexión fundamentada sobre el enfoque
5. **Conclusiones**: Síntesis de ideas principales
6. **Referencias**: Bibliografía en formato APA 7

## Bibliografía Utilizada

### Obligatoria
- Ibáñez y Mudarra (2014) - Texto básico (pp. 200 y siguientes)
- García-Sánchez et al. (2014) - Atención temprana centrada en la familia

### Complementaria
- Plena Inclusión (2024) - Informe situación AT en España
- Consenso Estatal AT (2025) - Hoja de ruta y estándares de calidad
- Díaz-Sánchez (2019) - Guía básica sobre AT y transformación
- Dunst et al. (2007) - Meta-análisis de prácticas centradas en familia
- McWilliam (2010) - Intervención basada en rutinas
- Otros artículos científicos de referencia

## Resultados de Aprendizaje

**RA1**: Conoce los conceptos fundamentales y principios básicos de la Atención Temprana para la inclusión de niños y niñas en su contexto sociofamiliar.

## Formato de Entrega

- **Formatos**: PDF y/o HTML
- **Fuente**: 12 puntos
- **Interlineado**: 1.5
- **Márgenes**: 2.5 cm
- **Referencias**: APA 7ª edición
- **Sin límite de extensión**: Prima calidad sobre cantidad

## Autor

**Juan Marcos García Aranzábal**  
UNED - Máster en Formación del Profesorado de ESO y Bachillerato, FP y Enseñanza de Idiomas  
Especialidad: Orientación Educativa

## Fecha

Noviembre de 2025

## Notas

- El documento responde a ambas preguntas planteadas en la actividad
- Todas las afirmaciones están justificadas con referencias bibliográficas
- Se incluye reflexión crítica personal fundamentada
- El enfoque es tanto teórico como práctico
- Se relacionan conceptos de diferentes fuentes bibliográficas
