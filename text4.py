#Remove Stop Word

text = 'the product is good and the service is fast'

stop_words = {'the','is','and'}

tokens = text.split()

filtered = [word for word in tokens if word not in stop_words]# list compherening
print(filtered) 