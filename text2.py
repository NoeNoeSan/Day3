import re

text = " AI IS AMAZITION!!!  NLP is useful. "

text = text.lower()
print(text)

text = re.sub(r"[^\w\s]","",text) # r = row text  
print(text)

text = re.sub(r"\s+"," ",text)
print(text)