import streamlit as st
import requests
import os
from faq_chatbot import FAQChatbot  # Import your chatbot class
from document_loader import DocumentLoader  # Assuming you have a loader class
from boltiotai import openai
from openai import OpenAI
from openai_service import OpenAIService

os.environ['OPENAI_API_KEY'] = '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'

# Set your OpenAI API key
# Check if the OPENAI_API_KEY is loaded correctly
api_key = os.environ.get('OPENAI_API_KEY')

if api_key is None:
    print("Error: OPENAI_API_KEY is not found in the environment.")
else:
    print("API Key loaded successfully!")

# Set the OpenAI API key from environment variables if it was found
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)

# Base folder where you expect `faq_data` to be
BASE_DIR = os.getcwd()  # or use a fixed directory like os.path.expanduser("~")

# Recursively search for `faq_data` in BASE_DIR
def find_faq_data(base_path):
    for root, dirs, _ in os.walk(base_path):
        if "faq_data" in dirs:
            return os.path.join(root, "faq_data")
    return None  # Return None if not found

# Get the actual `faq_data` path
DOCUMENTS_PATH = find_faq_data(BASE_DIR)

# Ensure the folder exists
if not os.path.exists(DOCUMENTS_PATH):
    raise FileNotFoundError(f"Error: The folder '{DOCUMENTS_PATH}' does not exist.")

# ✅ Pass the folder path when creating DocumentLoader
loader = DocumentLoader(DOCUMENTS_PATH)

# Initialize AI Service (Ensure it's correctly implemented)
ai_service = OpenAIService(client)  # Pass OpenAI client
# Initialize the chatbot
chatbot = FAQChatbot(loader, ai_service)

st.title("🤖 RAG Chatbot")

# Store chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    role, content = msg["role"], msg["content"]
    if role == "user":
        st.chat_message("user").write(content)
    else:
        st.chat_message("assistant").write(content)

# User input
user_input = st.chat_input("Type your question...")

if user_input:
    # Add user message
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Get response from chatbot
    bot_reply = chatbot.find_answer(user_input)

    # Add bot message
    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})
    st.chat_message("assistant").write(bot_reply)
