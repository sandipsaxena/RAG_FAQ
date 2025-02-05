import openai

# Set your OpenAI API key
openai.api_key = "your-api-key-here"

class OpenAIService:
    def query_openai(self, query, context):
        """Query OpenAI API with the document context"""
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI assistant that answers based on the provided documents."},
                {"role": "user", "content": f"Here is some document content: {context}\n\nQuestion: {query}"}
            ],
            max_tokens=300
        )
        return response["choices"][0]["message"]["content"]
