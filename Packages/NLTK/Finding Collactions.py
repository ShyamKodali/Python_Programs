import nltk
from nltk.book import *
from nltk import WordNetLemmatizer


# Lemmatized Words
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in text1]

# Converting Lemmatized Words list into a single text
new_text = nltk.Text(lemmatized_words)

# Finding Collactions 
new_text.collocations()