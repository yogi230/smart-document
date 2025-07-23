from sentence_transformers import SentenceTransformer


class Embeddings:
  def __init__(self, model="Qwen/Qwen3-Embedding-0.6B"):
    self.model = SentenceTransformer(model)

  def create_embeddings(self, text):
    return self.model.encode(text)
  

  def similarity(self, text1, text2):
    return self.model.similarity(text1, text2)