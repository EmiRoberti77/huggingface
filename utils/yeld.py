def filterOdd_withYield(numbers):
  for i in range(numbers):
    if(i%2!=0): 
       yield i

def filterOdd_withReturn(numbers):
  for i in range(numbers):
    if(i%2!=0): 
       return i

def filter_words(sentence:str):
  words = sentence.split(" ")
  for w in words:
    yield w



numbers_y = filterOdd_withYield(20)
numbers_r = filterOdd_withReturn(20)
words = filter_words("hello Emi's world of great coding")
print(list(words))
print(numbers_r)
print(list(numbers_y))

