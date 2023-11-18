from transformers import pipeline
from PDFReader import PDFReader
import constants

def split_document(document, chunk_size):
    words = document.split(' ')
    for i in range(0, len(words), chunk_size):
        yield ' '.join(words[i:i + chunk_size])

summarizer = pipeline(task="summarization", model="sshleifer/distilbart-cnn-12-6")

pdf = PDFReader(constants.DOCUMENT)
document = pdf.readPdf()

summaries = []
for chunk in split_document(document, 500):  # Adjust chunk size as needed
    chunk_summary = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
    if len(chunk_summary) > 0:
        summaries.append(chunk_summary[0]['summary_text'])


final_summary = ' '.join(summaries)
print(final_summary)