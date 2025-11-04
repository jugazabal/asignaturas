# PDF to Text Converter

Python tool for converting PDF files to text format using PyMuPDF and pypdf libraries.

## Installation

The required Python packages have been installed:
- `pypdf` - PDF text extraction
- `pymupdf` (fitz) - High-quality PDF processing
- `pytesseract` - OCR for scanned PDFs (requires Tesseract installation)
- `pdf2image` - Convert PDF pages to images
- `pillow` - Image processing

## Usage

### Basic Usage

Convert a PDF to text (creates .txt file with same name):
```bash
python pdf_to_text.py document.pdf
```

### Specify Output File

Convert with custom output filename:
```bash
python pdf_to_text.py document.pdf output.txt
```

### With Paths

Convert PDF in a specific folder:
```bash
python pdf_to_text.py "Primer cuatrimestre/Atencion temprana/document.pdf" "output.txt"
```

## Examples

### Convert Single File
```bash
python pdf_to_text.py "MONTANERO (2014).pdf"
```
This creates `MONTANERO (2014).txt` in the same folder.

### Convert to Specific Location
```bash
python pdf_to_text.py "Primer cuatrimestre/Asesoramiento psicopedagogico/Tareas/Tarea 2/MONTANERO (2014).pdf" "Montanero.txt"
```

### Batch Conversion (PowerShell)
```powershell
Get-ChildItem -Path . -Filter *.pdf -Recurse | ForEach-Object {
    python pdf_to_text.py $_.FullName
}
```

## Features

- **High-Quality Extraction**: Uses PyMuPDF for best text extraction quality
- **Fallback Support**: Automatically uses pypdf if PyMuPDF fails
- **Page Markers**: Adds `--- Page X ---` markers for navigation
- **Statistics**: Shows character, word, and line counts
- **Unicode Support**: Full UTF-8 encoding support
- **Error Handling**: Clear error messages and status reporting

## Output Format

The output text file includes:
- Page markers: `--- Page 1 ---`, `--- Page 2 ---`, etc.
- Extracted text preserving original formatting where possible
- UTF-8 encoding for international characters

## Troubleshooting

### No text extracted
- The PDF might be scanned images (needs OCR)
- Try opening the PDF to verify it contains selectable text

### OCR for Scanned PDFs
For scanned PDFs, you would need to install Tesseract OCR:
1. Download from: https://github.com/UB-Mannheim/tesseract/wiki
2. Install Tesseract
3. Add Tesseract to your PATH

### Permission Errors
- Ensure you have read access to the PDF file
- Ensure you have write access to the output directory

## Command-Line Help

```bash
python pdf_to_text.py
```
Shows usage information and examples.

## Integration with VS Code

You can run the script directly from VS Code:
1. Open Terminal in VS Code (Ctrl + `)
2. Navigate to the workspace folder
3. Run: `python pdf_to_text.py <your_pdf_file>`

## Python API Usage

You can also import and use the function in your own scripts:

```python
from pdf_to_text import pdf_to_text

# Convert PDF to text
output_path = pdf_to_text("document.pdf")

# Or specify output location
output_path = pdf_to_text("document.pdf", "custom_output.txt")
```

## Supported PDF Types

- ✅ Text-based PDFs (created from Word, LaTeX, etc.)
- ✅ PDFs with embedded fonts
- ✅ Multi-page documents
- ✅ PDFs with Unicode characters
- ⚠️ Scanned PDFs (requires OCR setup)
- ⚠️ Password-protected PDFs (not supported)

## Notes

- The tool preserves text content but may not perfectly preserve layout
- Tables and complex formatting may appear differently in text format
- For scanned PDFs, consider using OCR tools or online services
