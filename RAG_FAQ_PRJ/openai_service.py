import ollama
class OpenAIService:
    def __init__(self, model_name="gemma2:2b-instruct-q4_K_S"):
        self.use_local = False
        if self.use_local:
            try:
                import ollama
                self.client = ollama
                self.model_name = "gemma2:2b-instruct-q4_K_S"
            except ImportError:
                raise ImportError("Ollama not installed. Run `pip install ollama`")
        else:
            import openai
            self.client = openai

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
            if self.use_local:
                response = self.client.chat(model=self.model_name, messages=[{"role": "user", "content": prompt}])
                return {"answer": response["message"]["content"]}
            else:
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    stream=False,
                )
                return {"answer": response.choices[0].message.content}

        except Exception as e:
            return {"error": f"AI model error: {str(e)}"}
