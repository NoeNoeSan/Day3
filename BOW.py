from sklearn.feature_extraction.text import CountVectorizer

documents = [
    'AI is useful',
    'AI is powerful'
]

vectorizer = CountVectorizer() # CountVectorizer --- python transformer (Bag of word)
X = vectorizer.fit_transform(documents) # fit - train , fit_transform -- transform into numbers

print(vectorizer.get_feature_names_out())# 
print(X)
print(X.toarray())