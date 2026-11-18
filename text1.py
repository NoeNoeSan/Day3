text = 'The Product is good and effective.'

text = text.lower()
print(text)

if 'excellent' in text or 'useful' in text:
    print('Positive')
else:
    print("Negative")