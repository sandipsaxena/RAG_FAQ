import docx  # python-docx
from base_loader import BaseDocumentLoader

class DocxLoader(BaseDocumentLoader):
    def load_text(self, file_path):
        """Extract text from DOCX"""
        text = ""
        try:
            doc = docx.Document(file_path)
            text = "\n".join([para.text for para in doc.paragraphs])
        except Exception as e:
            print(f"Error reading DOCX {file_path}: {e}")
        return text
