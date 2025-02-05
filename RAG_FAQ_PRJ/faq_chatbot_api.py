from flask import Flask, request, jsonify
from faq_chatbot import FAQChatbot  
from document_loader import DocumentLoader
from openai_service import OpenAIService  # If using OpenAI

folder_path = "C:\\PythonVM\\RAG_FAQ\\RAG_FAQ_PRJ\\faq_data"

app = Flask(__name__)

# Initialize dependencies
loader     = DocumentLoader(folder_path)  # Ensure this class exists
ai_service = OpenAIService()  # Ensure this class exists

# Create chatbot instance with required dependencies
chatbot = FAQChatbot(loader, ai_service)

@app.route("/ask", methods=["POST"])
def ask_question():
    try:
        data = request.json
        user_question = data.get("question")

        if not user_question:
            return jsonify({"error": "Question is required"}), 400

        # Process question using chatbot
        response = chatbot.find_answer(user_question)
        
        return jsonify({"answer": response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def health_check():
    return jsonify({"status": "API is running"}), 200

if __name__ == "__main__":
    app.run(debug=True)
