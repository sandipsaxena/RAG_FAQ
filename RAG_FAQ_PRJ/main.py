from document_loader import DocumentLoader
from openai_service import OpenAIService
from faq_chatbot import FAQChatbot

if __name__ == "__main__":
    folder_path = "C:\\PythonVM\\RAG_FAQ\\RAG_FAQ_PRJ\\faq_data"
    # Initialize dependencies
    loader = DocumentLoader(folder_path)  # Load documents once
    ai_service = OpenAIService()  # OpenAI API service
    chatbot = FAQChatbot(loader, ai_service)

    # Sample query
    query = "How do I reset my password?"
    answer = chatbot.find_answer(query)
    print(answer)
