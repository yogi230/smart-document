from app.services.pdf_processor import PDFProcessor
import os

def main():
  pdf_path = os.path.join(os.path.dirname(__file__), "data", "cpumemory.pdf")
  PDFProcessor().process(pdf_path=pdf_path)

if __name__ == "__main__":
  main()