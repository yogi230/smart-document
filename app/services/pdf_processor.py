from PyPDF2 import PdfReader

class PDFProcessor:
  def __init__(self):
    pass

  def extract_text(self, pdf_path):
    pdf = PdfReader(pdf_path)
    return pdf.pages[0].extract_text()
