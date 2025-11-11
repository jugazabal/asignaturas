#!/usr/bin/env python3
"""
PDF to Text Converter
Extracts text from PDF files using PyMuPDF (fitz) with fallback to PyPDF.
Supports both text-based PDFs and scanned PDFs with OCR capability.

Usage:
    python pdf_to_text.py <pdf_file> [output_file]
    
Examples:
    python pdf_to_text.py document.pdf
    python pdf_to_text.py document.pdf output.txt
    python pdf_to_text.py "path/to/document.pdf" "path/to/output.txt"
"""

import sys
import os
from pathlib import Path

try:
    import fitz  # PyMuPDF
    PYMUPDF_AVAILABLE = True
except ImportError:
    PYMUPDF_AVAILABLE = False
    print("Warning: PyMuPDF not available, falling back to pypdf")

try:
    from pypdf import PdfReader
    PYPDF_AVAILABLE = True
except ImportError:
    PYPDF_AVAILABLE = False


def extract_text_pymupdf(pdf_path):
    """Extract text from PDF using PyMuPDF (best quality)"""
    text_content = []
    
    try:
        doc = fitz.open(pdf_path)
        
        for page_num, page in enumerate(doc, 1):
            # Extract text from page
            page_text = page.get_text()
            
            if page_text.strip():
                text_content.append(f"--- Page {page_num} ---\n")
                text_content.append(page_text)
                text_content.append("\n")
        
        doc.close()
        return "".join(text_content)
    
    except Exception as e:
        print(f"Error with PyMuPDF: {e}")
        return None


def extract_text_pypdf(pdf_path):
    """Extract text from PDF using pypdf (fallback)"""
    text_content = []
    
    try:
        reader = PdfReader(pdf_path)
        
        for page_num, page in enumerate(reader.pages, 1):
            page_text = page.extract_text()
            
            if page_text.strip():
                text_content.append(f"--- Page {page_num} ---\n")
                text_content.append(page_text)
                text_content.append("\n")
        
        return "".join(text_content)
    
    except Exception as e:
        print(f"Error with pypdf: {e}")
        return None


def pdf_to_text(pdf_path, output_path=None):
    """
    Convert PDF to text file
    
    Args:
        pdf_path: Path to the PDF file
        output_path: Optional output text file path. If not provided, 
                    will use same name as PDF with .txt extension
    
    Returns:
        Path to the output text file
    """
    pdf_path = Path(pdf_path)
    
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    # Determine output path
    if output_path is None:
        output_path = pdf_path.with_suffix('.txt')
    else:
        output_path = Path(output_path)
    
    print(f"Converting: {pdf_path}")
    print(f"Output to: {output_path}")
    
    # Try PyMuPDF first (better quality)
    text = None
    if PYMUPDF_AVAILABLE:
        print("Using PyMuPDF for extraction...")
        text = extract_text_pymupdf(str(pdf_path))
    
    # Fallback to pypdf
    if text is None and PYPDF_AVAILABLE:
        print("Using pypdf for extraction...")
        text = extract_text_pypdf(str(pdf_path))
    
    if text is None:
        raise RuntimeError("Failed to extract text from PDF")
    
    # Save to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    
    # Print statistics
    num_chars = len(text)
    num_words = len(text.split())
    num_lines = text.count('\n')
    
    print(f"\nExtraction complete!")
    print(f"Characters: {num_chars:,}")
    print(f"Words: {num_words:,}")
    print(f"Lines: {num_lines:,}")
    
    return output_path


def main():
    """Command-line interface"""
    if len(sys.argv) < 2:
        print("Usage: python pdf_to_text.py <pdf_file> [output_file]")
        print("\nExamples:")
        print("  python pdf_to_text.py document.pdf")
        print('  python pdf_to_text.py document.pdf output.txt')
        print('  python pdf_to_text.py "path/to/document.pdf" "path/to/output.txt"')
        sys.exit(1)
    
    pdf_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        result = pdf_to_text(pdf_file, output_file)
        print(f"\n✓ Successfully converted to: {result}")
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
