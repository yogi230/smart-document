from PyPDF2 import PdfReader
from app.services.embeddings import embeddings
from app.services.vector_db import get_chroma_db

class PDFProcessor:
  def __init__(self):
    self.embeddings = embeddings
    self.chroma_db = get_chroma_db(persistent=True, path="./chroma_db", collection_name="pdf_collection")

  def process(self, pdf_path):
    pdf = PdfReader(pdf_path)
    text = "\n".join([pdf.pages[0].extract_text()])
    print("text: ", text)
    embeddings = self.embeddings.create_embeddings(text)
    print("embeddings: ", embeddings)

    a = self.chroma_db.add(ids=["1"], documents=[text], embeddings=[embeddings])
    print("a: ", a)
    query = "What is the main idea of the document?"
    query_embeddings = self.embeddings.create_embeddings(query)
    q = self.chroma_db.query(query_embeddings=query_embeddings)
    print("q: ", q)
    return True
