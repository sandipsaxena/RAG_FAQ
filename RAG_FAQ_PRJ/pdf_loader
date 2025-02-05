import fitz  # PyMuPDF
from base_loader import BaseDocumentLoader

class PDFLoader(BaseDocumentLoader):
    def load_text(self, file_path):
        """Extract text from PDF"""
        text = ""
        try:
            doc = fitz.open(file_path)
            for page in doc:
                text += page.get_text() + "\n"
        except Exception as e:
            print(f"Error reading PDF {file_path}: {e}")
        return text
