import os

from pdf_loader import PDFLoader
from docx_loader import DocxLoader
from txt_loader import TxtLoader

class DocumentLoader:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.loaders = {".pdf": PDFLoader(), ".docx": DocxLoader(), ".txt": TxtLoader()}  # Extendable
        self.documents = self.load_documents()  # Load docs at startup

    def load_documents(self):
        """Load all PDFs and DOCX files from the folder into memory"""
        documents = []
        for file_name in os.listdir(self.folder_path):
            file_ext = os.path.splitext(file_name)[1].lower()
            loader = self.loaders.get(file_ext)

            if loader:
                file_path = os.path.join(self.folder_path, file_name)
                documents.append({"file": file_name, "content": loader.load_text(file_path)})

        return documents
