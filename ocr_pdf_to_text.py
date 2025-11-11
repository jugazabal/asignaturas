import os
import pytesseract
from pdf2image import convert_from_path
from pathlib import Path

# Ruta al ejecutable de Tesseract (Windows installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\vijgia\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = r'C:\Users\vijgia\AppData\Local\Programs\Tesseract-OCR\tessdata'

pdf_path = r"C:\Users\vijgia\OneDrive - Vitec Software Group AB (publ)\Documentos\UNED\Asignaturas\Primer cuatrimestre\Diagnostico\textos\CAPITULO 1 DIAGNOSTICO.pdf"
output_txt = r"C:\Users\vijgia\OneDrive - Vitec Software Group AB (publ)\Documentos\UNED\Asignaturas\Primer cuatrimestre\Diagnostico\textos\CAPITULO 1 DIAGNOSTICO.txt"

images = convert_from_path(pdf_path, poppler_path=r"C:\Users\vijgia\OneDrive - Vitec Software Group AB (publ)\Escritorio\Cajon\poppler-25.07.0\Library\bin")
full_text = ""
for i, img in enumerate(images):
    text = pytesseract.image_to_string(img, lang='spa')
    full_text += f"\n--- Page {i+1} ---\n{text}\n"

with open(output_txt, "w", encoding="utf-8") as f:
    f.write(full_text)

print(f"OCR extraction complete! Text saved to {output_txt}")