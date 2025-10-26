"""
PDF Reader Module - Extract text from PDF files
"""

import PyPDF2
import pdfplumber
from typing import List, Optional
import logging

logger = logging.getLogger(__name__)


class PDFReader:
    """Extract text from PDF documents."""
    
    def __init__(self, pdf_path: str, method: str = "pdfplumber"):
        """
        Initialize PDF reader.
        
        Args:
            pdf_path: Path to the PDF file
            method: Extraction method ('pdfplumber' or 'pypdf2')
        """
        self.pdf_path = pdf_path
        self.method = method
        self.text = None
        
    def extract_text(self) -> str:
        """
        Extract all text from the PDF.
        
        Returns:
            Extracted text as a string
        """
        if self.method == "pdfplumber":
            return self._extract_with_pdfplumber()
        else:
            return self._extract_with_pypdf2()
    
    def _extract_with_pdfplumber(self) -> str:
        """Extract text using pdfplumber (better for complex layouts)."""
        try:
            text = ""
            with pdfplumber.open(self.pdf_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
            self.text = text.strip()
            logger.info(f"Extracted {len(self.text)} characters from PDF")
            return self.text
        except Exception as e:
            logger.error(f"Error extracting text with pdfplumber: {e}")
            return ""
    
    def _extract_with_pypdf2(self) -> str:
        """Extract text using PyPDF2 (fallback method)."""
        try:
            text = ""
            with open(self.pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
            self.text = text.strip()
            logger.info(f"Extracted {len(self.text)} characters from PDF")
            return self.text
        except Exception as e:
            logger.error(f"Error extracting text with PyPDF2: {e}")
            return ""
    
    def get_page_count(self) -> int:
        """Get the total number of pages in the PDF."""
        try:
            with pdfplumber.open(self.pdf_path) as pdf:
                return len(pdf.pages)
        except Exception as e:
            logger.error(f"Error getting page count: {e}")
            return 0
