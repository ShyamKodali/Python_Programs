import nltk 

from nltk.tokenize import word_tokenize

string = """ If you wish to make an apple pie from scratch,
             you must first invent the universe."""
             
             
Tokenize_String = word_tokenize(string)

# Tagging Parts of Speech to the Tokenized String

Tagging_POS = nltk.pos_tag(Tokenize_String)
print(Tagging_POS)