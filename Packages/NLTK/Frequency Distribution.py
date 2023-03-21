import nltk
from nltk import FreqDist
from nltk.book import *
from nltk import word_tokenize

# Removing Stop Words

stop_words = set(nltk.corpus.stopwords.words("english"))

meaningful_words = []
for word in text5:
    if word.casefold() not in stop_words:
        meaningful_words.append(word)
        
print(meaningful_words)
print("**************************************************************************************************************")

# Creating Frequency Distribution 

Frequency_Distribution = FreqDist(meaningful_words)
print(Frequency_Distribution.most_common(20))

# Plotting Frequnecy Distribution 

Frequency_Distribution.plot(20, cumulative=True)