# Word Tokenization 

text = 'AI makes applications intelligent.'

tokens = text.lower().replace(".","").split() #replace() only this place
print(tokens)