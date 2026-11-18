import re
text = "  AI Applications Are VERY Useful!!! NLP is interesting.  "

text = text.lower()
print(text)
text = re.sub(r"[^\w\s]", "",text)
print(text)
text = re.sub(r"\s+"," ",text)
print(text)
tokens = text.replace(".","").split()
print(tokens)
stop_word = {"the", "is", "and","are"}
filtered = [word for word in tokens if word not in stop_word ]
print(filtered)