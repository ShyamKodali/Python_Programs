import nltk

# Importing Tokenizers 
from nltk.tokenize import word_tokenize

# Importing Porter Stemmer for Pluralised Words
from nltk.stem.porter import PorterStemmer

# Importing Snowball Stemmer for Unit Testing 
from nltk.stem.snowball import SnowballStemmer


stemmer_1 = PorterStemmer()
# SnoballStemmer is the Updated form of Porter Stemmer method
stemmer_2 = SnowballStemmer(language="english")

string = """ The crew of the USS Discovery discovered many discoveries.
             Discovering is what explorers do."""

# Tokenizing defined string by word

Tok_by_word = word_tokenize(string)
print(Tok_by_word)
print('*********************************************************************************************************')

# Filtering Stop Words 

stop_words = set(nltk.corpus.stopwords.words("english"))
Filtered_Tok_by_word = []

for word in Tok_by_word:
    if word.casefold() not in stop_words:
        Filtered_Tok_by_word.append(word)
print(Filtered_Tok_by_word)
print('*********************************************************************************************************')

# Stemming the Tokenized string (Tok_by_word) using Porter Stemmer 


stemmed_string_1 = [stemmer_1.stem(word) for word in Tok_by_word]  
print(stemmed_string_1)
print('*********************************************************************************************************')

# Stemming the Tokenized string (Filtered_Tok_by_word) using Snowball Stemmer 

stemmed_string_2 = [stemmer_2.stem(word) for word in Filtered_Tok_by_word]
print(stemmed_string_2)