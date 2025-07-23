from PyPDF2 import PdfReader
from app.services.embeddings import embeddings
from app.services.vector_db import get_chroma_db
from app.services.gemini import get_gemini_instance

class PDFProcessor:
  def __init__(self):
    self.embeddings = embeddings
    self.chroma_db = get_chroma_db(persistent=True, path="./chroma_db", collection_name="pdf_collection")
    self.gemini = get_gemini_instance()

  def process(self, pdf_path):
    with open(pdf_path, "rb") as file:
      pdf = PdfReader(file)
      for i, page in enumerate(pdf.pages):
        embedding_id = str(i)
        if self.chroma_db.get(ids=[embedding_id], include=[]):
          continue
        text = page.extract_text()
        # print("text index: ", i)
        embeddings = self.embeddings.create_embeddings(text)
        # print("embeddings index: ", i, " ", embeddings)
        self.chroma_db.add(ids=[embedding_id], documents=[text], embeddings=[embeddings])

    query = "What is the document about? can you please explain in hindi"
    query_embeddings = self.embeddings.create_embeddings(query)
    retrieved_docs = self.chroma_db.query(query_embeddings=query_embeddings)
    # print("retrieved_docs: ", retrieved_docs)

    context = "\n\n".join(retrieved_docs["documents"][0])
    response = self.gemini.generate_text(query=query, context=context)
    print("response: ", response)

    return True
