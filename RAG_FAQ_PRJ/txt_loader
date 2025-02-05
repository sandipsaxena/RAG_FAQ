from base_loader import BaseDocumentLoader

class TxtLoader(BaseDocumentLoader):
    def load_text(self, file_path):
        """Extract text from a TXT file"""
        text = ""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
        except Exception as e:
            print(f"Error reading TXT {file_path}: {e}")
        return text
