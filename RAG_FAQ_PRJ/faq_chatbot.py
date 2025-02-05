
from boltiotai import openai

class FAQChatbot:
    def __init__(self, loader, ai_service):
        self.documents = loader.documents  # Loaded documents in memory
        self.ai_service = ai_service

    def find_answer(self, query):
        """Find relevant document and ask OpenAI"""
        if not self.documents:
            return "No documents found."

        # Combine all document content (can be improved with a search algorithm)
        combined_text = "\n".join([doc["content"] for doc in self.documents])

        # Send to OpenAI for processing
        return self.ai_service.query_openai(query, combined_text)
