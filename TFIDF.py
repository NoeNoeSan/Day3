from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    'AI improves learning',
    'AI improves bussiness'
]

vectorizer = TfidfVectorizer()# Only different CountVertoizer()
X = vectorizer.fit_transform(documents)

print(vectorizer.get_feature_names_out())
print(X.toarray())# TFIDF is more exactly than BOW
