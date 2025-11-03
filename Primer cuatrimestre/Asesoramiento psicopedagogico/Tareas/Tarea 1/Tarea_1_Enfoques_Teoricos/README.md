# Proyecto Quarto: Tarea 1 - Fichas Resumen de Enfoques Teóricos

## 📁 Estructura del Proyecto

Este proyecto contiene todos los archivos necesarios para desarrollar la Tarea 1 de Asesoramiento Psicopedagógico usando Quarto con formato APA.

```
Tarea_1_Enfoques_Teoricos/
├── tarea1.qmd              # Documento principal (EDITAR AQUÍ)
├── _quarto.yml             # Configuración del proyecto
├── apa.csl                 # Estilo de citación APA
├── references.bib          # Bibliografía (AÑADIR REFERENCIAS)
└── README.md               # Este archivo
```

## 🚀 Inicio Rápido

### 1. Completar el contenido

1. **Abre `tarea1.qmd`** en VS Code
2. **Completa** las secciones marcadas con `[Desarrollar...]` usando la bibliografía básica del curso
3. **Añade tus referencias** bibliográficas en `references.bib`
4. **Personaliza** el nombre del autor en el encabezado YAML

### 2. Vista previa en tiempo real

```bash
quarto preview tarea1.qmd
```

Esto abrirá una ventana del navegador que se actualiza automáticamente al guardar cambios.

### 3. Generar el documento final

#### Para PDF (entregar en la UNED):
```bash
quarto render tarea1.qmd --to pdf
```

#### Para HTML (consulta personal):
```bash
quarto render tarea1.qmd --to html
```

#### Ambos formatos:
```bash
quarto render tarea1.qmd
```

Los archivos generados estarán en la carpeta `_output/`

## 📝 Cómo Editar

### Añadir referencias bibliográficas

1. Abre `references.bib`
2. Añade tus referencias siguiendo el formato BibTeX (hay ejemplos en el archivo)
3. Cada referencia necesita un identificador único (ej: `lopez2020`)

### Citar en el texto

- **Cita narrativa**: `@lopez2020` → López (2020)
- **Cita entre paréntesis**: `[@lopez2020]` → (López, 2020)
- **Múltiples citas**: `[@lopez2020; @garcia2019]` → (López, 2020; García, 2019)
- **Con página**: `[@lopez2020, p. 45]` → (López, 2020, p. 45)

### Estructura del contenido

El archivo `tarea1.qmd` ya tiene la estructura completa:

1. ✅ Resumen (150-250 palabras)
2. ✅ Introducción con objetivos
3. ✅ Perspectivas teóricas (4 perspectivas con sus enfoques)
4. ✅ Análisis comparativo
5. ✅ Conclusiones
6. ✅ Referencias (se generan automáticamente)

**Solo necesitas completar las secciones con tu contenido basado en la bibliografía del curso.**

## ✅ Checklist antes de Entregar

### Contenido
- [ ] Todas las secciones `[Desarrollar...]` están completas
- [ ] El nombre del autor está personalizado
- [ ] Resumen entre 150-250 palabras
- [ ] Las 4 perspectivas están completas con sus 7 apartados cada una
- [ ] Valoración crítica personal en cada enfoque
- [ ] Ejemplos contextualizados en el sistema educativo español

### Formato
- [ ] El PDF tiene máximo 6 páginas (sin contar referencias)
- [ ] Fuente 12pt, márgenes 2.5cm, interlineado 1.5 (ya configurado)
- [ ] Estilo académico en tercera persona
- [ ] Sin errores ortográficos

### Referencias
- [ ] Todas las citas tienen su referencia en `references.bib`
- [ ] Todas las referencias están citadas en el texto
- [ ] Formato APA correcto (se genera automáticamente)

### Final
- [ ] Archivo PDF generado y revisado
- [ ] Extensión no superior a 6 páginas
- [ ] Listo para subir al curso virtual

## 🛠️ Solución de Problemas

### Error: "No se encuentra quarto"
Instala Quarto desde: https://quarto.org/docs/get-started/

### Error al generar PDF
Instala TinyTeX:
```bash
quarto install tinytex
```

### Las referencias no aparecen
1. Verifica que `references.bib` tenga las referencias
2. Asegúrate de citar las referencias en el texto
3. Verifica que `apa.csl` exista en la carpeta

### El documento tiene más de 6 páginas
1. Reduce el texto en las secciones más extensas
2. Sé más conciso en las descripciones
3. Elimina ejemplos redundantes

## 📚 Recursos

- **Guía Quarto**: https://quarto.org/docs/guide/
- **Formato APA**: Ver `apa_guidelines.md` en la carpeta superior
- **Bibliografía básica**: Disponible en el curso virtual (Tema 1)
- **BibTeX Generator**: https://www.bibtex.com/

## 💡 Consejos

1. **Trabaja por secciones**: Completa una perspectiva antes de pasar a la siguiente
2. **Usa vista previa**: `quarto preview` te permite ver cambios en tiempo real
3. **Guarda frecuentemente**: Haz commits en Git si usas control de versiones
4. **Revisa el PDF**: Genera el PDF periódicamente para verificar extensión
5. **Consulta la bibliografía**: Basa tus respuestas en el material del curso

## ⚠️ Importante

- Este trabajo debe ser **original y personal**
- Se utilizan herramientas antiplagio (Compilatio y Verificatio)
- Cita correctamente todas las fuentes
- No copies de compañeros o de Internet

---

**¡Éxito con tu tarea!** 🎓

Si tienes dudas sobre Quarto o el formato, consulta la documentación o el foro del curso.
