import nltk
from nltk import corpus



string = ''' Sir, I protest. I am not a merry man!'''

# Tokenizing by word 

Tok_by_Word = nltk.word_tokenize(string)
print(Tok_by_Word)
print('*****************************************************************************')


# Creating Set of Stop Words from "English Lang"

stop_words = set(nltk.corpus.stopwords.words('english'))


# Filtering Stop words from Tok_by_Word and Storing in New_Tok_by_Word 

New_Tok_by_Word = [] 

for word in Tok_by_Word:
    if word.casefold() not in stop_words:
        New_Tok_by_Word.append(word)
        
print(New_Tok_by_Word)
print('*****************************************************************************')
