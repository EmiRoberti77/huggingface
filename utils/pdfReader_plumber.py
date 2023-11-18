import pdfplumber

class PdfReader():

  def extractPdfPages(self):
    with pdfplumber.open('documents/retail_report.pdf', 'rb') as pdf:
      for page in pdf.pages:
        print(page.extract_text())

pdf = PdfReader()
pdf.extractPdfPages()