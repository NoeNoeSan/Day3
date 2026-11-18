from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline # train and transform into numerical
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score # 

texts = [    
    "I love this product",
    "The service is excellent",    
    "This is a wonderful experience",    
    "I am very happy with the purchase",    
    "The product is fantastic",    
    "I really like this service",    
    "I hate this product",    
    "The service is terrible",    
    "This is a bad experience",    
    "I am very disappointed",    
    "The product is awful",    
    "I do not like this service" ]

labels = [    
    "Positive", 
    "Positive", 
    "Positive",    
    "Positive", 
    "Positive", 
    "Positive",    
    "Negative", 
    "Negative", 
    "Negative",    
    "Negative", 
    "Negative", 
    "Negative" ]

X_train,X_test,y_train,y_test = train_test_split(texts, labels, test_size = 0.25)
model = Pipeline([
    ('tfidf',TfidfVectorizer()),        #just call / declaring
    ('classifier', MultinomialNB())
])  

model.fit(X_train,y_train)  #model is both transform and train so use fit not fit.transform
prediction = model.predict(X_test)
print(prediction)
print(y_test)
print("Testing Accuracy :",accuracy_score(y_test,prediction))

prediction2 = model.predict(X_train)
print(prediction2)
print(y_train)
print("Training Accuracy :",accuracy_score(y_train,prediction2))

new_text = ['This product is excellent']

print(model.predict(new_text))# if he know words he'll write