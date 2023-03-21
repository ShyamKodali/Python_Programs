import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag



string = """Men like Schiaparelli watched the red planet—it is odd, by-the-bye, that
            for countless centuries Mars has been the star of war—but failed to
            interpret the fluctuating appearances of the markings they mapped so well.
            All that time the Martians must have been getting ready.
            During the opposition of 1894 a great light was seen on the illuminated
            part of the disk, first at the Lick Observatory, then by Perrotin of Nice,
            and then by other observers. English readers heard of it first in the
            issue of Nature dated August 2."""

# Creating a function for NRE 
def extract_ne(quote):
    # Tokenizing String
    tok_string = word_tokenize(quote)
    # Parts of Speech for the Tokenized String
    pos_tok_string = pos_tag(tok_string)
    # Creating Tree for NRE - Named Entity Recognistion  
    tree = nltk.ne_chunk(pos_tok_string, binary=True)
    NRE = set(" ".join(i[0] for i in t) for t in tree if hasattr(t, "label") and t.label() == "NE")
    return NRE


print(extract_ne(string))