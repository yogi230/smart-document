from sentence_transformers import SentenceTransformer


class Embeddings:
  def __init__(self, model_name="Qwen/Qwen3-Embedding-0.6B"):
    self.model = SentenceTransformer(model_name)

  _instance = None

  @classmethod
  def get_instance(cls) -> 'Embeddings':
    """
    Get singleton instance of the Embeddings class

    Returns:
      Embeddings: Singleton instance of the Embeddings class
    """
    if cls._instance is None:
      cls._instance = cls()
    return cls._instance

  def create_embeddings(self, text: str) -> list[float]:
    """
    Create embeddings for the given text

    Args:
      text: str

    Returns:
      list[float]: Embeddings for the given text
    """
    return self.model.encode(text)
  

  def similarity(self, text1: str, text2: str) -> float:
    """
    Calculate similarity between two texts

    Args:
      text1: str
      text2: str

    Returns:
      float: Similarity between the two texts
    """
    return self.model.similarity(text1, text2)

embeddings = Embeddings.get_instance()