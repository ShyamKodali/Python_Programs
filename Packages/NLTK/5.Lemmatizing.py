import nltk
from nltk import word_tokenize
from nltk import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

string = """ The friends of DeSoto love scarves. """


Tokenize_String = word_tokenize(string)
print(Tokenize_String)
print('**********************************************************')

# Lemmatizing to the Tokenized String

Lemmatized_String = [lemmatizer.lemmatize(word) for word in Tokenize_String]
print(Lemmatized_String)


