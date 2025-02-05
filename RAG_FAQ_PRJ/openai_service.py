import os
from boltiotai import openai 
from  openai import OpenAI
from dotenv import load_dotenv, find_dotenv
from openai import Client
from flask import Flask, render_template_string, request

os.environ['OPENAI_API_KEY'] = 'V45etSteeKvvHZxh2UbOE4-g91iqRjNZSHOAsIbZWPY'

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
class OpenAIService:
    def query_openai(self, user_query: str, documents: str):
        """Query OpenAI API with the document context"""
        response = client.completions.create(
                model="gpt-4o-mini",
                prompt=f"You are an AI assistant that answers based on the provided documents. User query: {user_query}",
                max_tokens=300
        )
        return response["choices"][0]["message"]["content"]
