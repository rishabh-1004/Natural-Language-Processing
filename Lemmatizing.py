from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print (lemmatizer.lemmatize("cats")) #Output - cat
print (lemmatizer.lemmatize("cacti")) #Output - cactus
print (lemmatizer.lemmatize("geese")) #Output - goose
print (lemmatizer.lemmatize("rocks")) #Output - rock
print (lemmatizer.lemmatize("python")) #Output - python


# By Default pos is noun we can change that too
print (lemmatizer.lemmatize("better")) #Output - better
print (lemmatizer.lemmatize("better",pos="a")) #Output - good
print (lemmatizer.lemmatize("best",pos="a")) #Output - best

