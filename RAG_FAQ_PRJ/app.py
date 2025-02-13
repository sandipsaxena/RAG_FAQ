import streamlit as st
from datetime import datetime, timedelta
import requests
import os
from faq_chatbot import FAQChatbot  
from document_loader import DocumentLoader  
from boltiotai import openai
from openai import OpenAI
from openai_service import OpenAIService
from dotenv import load_dotenv

# Set your OpenAI API key# Load environment variables from raq_env.env
load_dotenv()

# Get the API key
api_key = os.getenv("OPENAI_API_KEY")

# Check if the OPENAI_API_KEY is loaded correctly
if api_key is None:
    print("Error: OPENAI_API_KEY is not found in the environment.")
else:
    print("API Key loaded successfully!")

# Set the OpenAI API key from environment variables if it was found
client = OpenAI(api_key=api_key)

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

# Custom CSS to remove button backgrounds
st.markdown("""
    <style>
    /* Remove background from buttons */
    .stButton > button {
        background-color: transparent !important;
        border: none !important;
        color: black !important;
        text-align: left !important;
        font-size: 16px !important;
        padding: 5px 10px !important;
    }
    
    /* Adjust expander text color */
    .st-expander {
        background-color: transparent !important;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for title if not set
if "app_title" not in st.session_state:
    st.session_state.app_title = "🤖 RAG GuideBot"

# Sidebar with rename option inside an expander (collapsible box)
with st.sidebar:
    with st.expander("⚙️ Rename Chatbot"):
        new_title = st.text_input("", st.session_state.app_title)
        if new_title.strip():  # Prevent empty names
            st.session_state.app_title = new_title.strip()  # Update title dynamically

# Display the title with the latest name
st.title(st.session_state.app_title)

# Store chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar for chat history & new chat button
with st.sidebar:
    st.title("📜 Chat History")
    

    def get_date_label(date_str):
        chat_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        today = datetime.today().date()
        yesterday = today - timedelta(days=1)

        if chat_date == today:
            return "Today"
        elif chat_date == yesterday:
            return "Yesterday"
        else:
            return chat_date.strftime("%d %b %Y")

    grouped_chats = {}
    for chat in st.session_state.chat_history:
        label = get_date_label(chat["date"])
        if label not in grouped_chats:
            grouped_chats[label] = []
        grouped_chats[label].append(chat)

    for date_label, chats in grouped_chats.items():
        st.markdown(f'<div class="date-header">{date_label}</div>', unsafe_allow_html=True)
        for index, chat in enumerate(chats):
            chat_name = chat["name"]
            key = f"chat_{index}"
            chat_html = f"""
                <div class="chat-history" onclick="window.location.reload();">
                    <img src="https://via.placeholder.com/25" alt="chat_icon">
                    <span>{chat_name}</span>
                </div>
            """
            if st.button(chat_name, key=key):
                st.session_state.messages = chat["messages"]
                st.rerun()
    
    # Button to start a new chat
    if st.button("🆕 New Chat"):
        if st.session_state.messages:
            first_question = st.session_state.messages[0]["content"]
            chat_title = " ".join(first_question.split()[:3]).capitalize()
            st.session_state.chat_history.append({
                "name": chat_title,
                "messages": st.session_state.messages,
                "date": datetime.today().strftime("%Y-%m-%d")
            })
        st.session_state.messages = []
        st.rerun()

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
