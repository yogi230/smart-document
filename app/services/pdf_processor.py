from PyPDF2 import PdfReader
from app.services.embeddings import Embeddings

class PDFProcessor:
  def __init__(self):
    self.embeddings = Embeddings()

  def process(self, pdf_path):
    pdf = PdfReader(pdf_path)
    text = "\n".join([pdf.pages[0].extract_text()])
    print("text: ", text)
    embeddings = self.embeddings.create_embeddings(text)
    print("embeddings: ", embeddings)
    return True
