from google import genai
import dotenv
import os

class Gemini:
  def __init__(self, api_key: str):
    try:
      self.client = genai.Client(api_key=api_key)
    except Exception as e:
      raise e

  _instance = None

  @classmethod
  def get_instance(cls, api_key: str):
    if cls._instance is None:
      cls._instance = cls(api_key=api_key)
    return cls._instance

  def generate_text(self, model: str = "gemini-1.5-flash", query: str = None, context: str = None) -> str:
    prompt = self._generate_prompt(query, context)
    response = self.client.models.generate_content(model=model, contents=prompt)
    return response.text
  
  def _generate_prompt(self, query: str, context: str) -> str:
    return f"""
    You are a helpful assistant that can answer questions and help with tasks.
    You are given a query and a context.
    You need to answer the query based on the context.
    Answer should be concise and within hard limit of 100 words, do not use any abusive language and be calm, humble and professional.
    if you are not sure about the answer, say you don't know. Do not make up any information without any supporting source text.
    Consider the context below to answer the query.
    Context: {context}

    Query: {query}
    """
  

def get_gemini_instance():
  dotenv.load_dotenv()
  api_key = os.getenv("GEMINI_API_KEY")
  return Gemini.get_instance(api_key=api_key)