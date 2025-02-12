class OpenAIService:
    def __init__(self, client):
        self.client = client  # Use the existing client

    def query_openai(self, user_query: str, documents: str):
        """Query OpenAI API with the document context"""
        #prompt = f"Use the following document context to answer the question:\n\n{documents}\n\nQuestion: {user_query}"
        if documents.strip():  # Check if documents contain any meaningful content
         prompt = f"""Use the following document context to answer the question.
                    Based on the provided documents, answer concisely.

                    Document Context:
                    {documents}

        Question: {user_query}""".strip()
        else:
         prompt = f"""The provided documents do not contain information relevant to the question.
                 Use your general knowledge to generate a helpful answer.

                 Question: {user_query}""".strip()

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            stream=False,
        )
        return {"answer": response.choices[0].message.content}
