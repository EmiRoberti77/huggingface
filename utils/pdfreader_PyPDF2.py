import PyPDF2 as pdf
import os

class PDFReader():
  def __init__(self, document) -> None:
     self.document = document
     
  def readPdf(self)->str:
    document = ""
    try:
      with open(self.document, 'rb') as file:
        reader = pdf.PdfReader(file)
        for page in reader.pages:
            document += page.extract_text()
    except Exception as e:
       print(e)
       raise Exception(f"error reading {self.document}")

    return document
      
# p = PDFReader('documents/retail_report.pdf')
# document = p.readPdf()
# print(document)

