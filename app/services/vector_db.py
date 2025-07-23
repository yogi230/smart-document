import chromadb
from chromadb.api.types import QueryResult, GetResult

class VectorDB:

  _instance = None

  def __init__(self, persistent: bool = False, path: str = None, collection_name: str = "pdf_collection"):
    try:
      if persistent:
        self.client = chromadb.PersistentClient(path=path)
      else:
        self.client = chromadb.Client()
      self.collection = self.client.get_or_create_collection(name=collection_name)
    except Exception as e:
      raise e
   

  @classmethod
  def get_instance(cls, persistent: bool = False, path: str = None, collection_name: str = "pdf_collection"):
    """
    Get the instance of the VectorDB class

    Args:
      persistent: bool
        - If True, the database will be persistent and stored in the path
        - If False, the database will be in memory and will be lost when the program is closed
      path: str
        - If persistent is True, the path to the database
      collection_name: str
        - The name of the collection to use

    Returns:  
      VectorDB: Instance of the VectorDB class
    """
    if cls._instance is None:
      cls._instance = cls(persistent=persistent, path=path, collection_name=collection_name)
    return cls._instance

  def add(self, ids: list[str], documents: list[str], embeddings: list[list[float]]) -> None:
    """
    Add documents to the collection

    Args:
      ids: list[str]
        - The ids of the documents to add
      documents: list[str]
        - The documents to add
      embeddings: list[list[float]]
        - The embeddings of the documents to add

    Returns:
      None
    """
    self.collection.add(documents=documents, ids=ids, embeddings=embeddings)

  def query(self, query_embeddings: list[float], n_results: int = 4) -> QueryResult:
    """
    Query the collection

    Args:
      query_embeddings: list[float]
        - The embeddings of the query
      n_results: int
        - The number of results to return

    Returns:
      QueryResult: The results of the query
    """
    return self.collection.query(query_embeddings=[query_embeddings], n_results=n_results)
  
  def get(self, ids: list[str], include: list[str] = ["documents", "metadatas"]) -> GetResult:
    """
    Get the documents and metadatas for the given ids

    Args:
      ids: list[str]
        - The ids to check

    Returns:
      GetResult: The results of the get
    """
    return self.collection.get(ids=ids, include=include)


def get_chroma_db(persistent: bool = False, path: str = None, collection_name: str = "pdf_collection") -> VectorDB:
  """
  Get the instance of the VectorDB class

  Args:
    persistent: bool
    path: str
    collection_name: str

  Returns:
    VectorDB: Instance of the VectorDB class
  """
  return VectorDB.get_instance(persistent=persistent, path=path, collection_name=collection_name)