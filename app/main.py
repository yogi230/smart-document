from app.services.pdf_processor import PDFProcessor
import os

def main():
  pdf_path = os.path.join(os.path.dirname(__file__), "data", "cpumemory.pdf")
  text = PDFProcessor().extract_text(pdf_path=pdf_path)
  print(text)

if __name__ == "__main__":
  main()