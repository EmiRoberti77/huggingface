from transformers import pipeline
import content

summarizer = pipeline(task="summarization", model="sshleifer/distilbart-cnn-12-6")
result = summarizer(content.article, max_length=130,min_length=30, do_sample=False)
if len(result) > 0:
  print(result[0]['summary_text'])
else:
  print("not summarized")