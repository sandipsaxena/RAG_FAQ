class OpenAIService:
    def __init__(self, client):
        self.client = client  # Use the existing client

    def query_openai(self, user_query: str, documents: str):
        """Query OpenAI API with the document context while handling token limits."""
        
        # Limit document length to prevent token overflow (approx. 4000 chars)
        MAX_DOC_LENGTH = 4000  
        documents = documents[:MAX_DOC_LENGTH].strip() if documents else ""

        if documents:
            prompt = f"""Use the following document context to answer the question.
                    Based on the provided documents, answer concisely.

                    Document Context:
                    {documents}

                    Question: {user_query}""".strip()
        else:
            prompt = f"""The provided documents do not contain information relevant to the question.
                    Use your general knowledge to generate a helpful answer.

                    Question: {user_query}""".strip()

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                stream=False,
            )
            return {"answer": response.choices[0].message.content}
        
        except Exception as e:
            return {"error": f"OpenAI API error: {str(e)}"}
