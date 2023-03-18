import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag



string = """If you wish to make an apple pie from scratch,
             you must first invent the universe."""

# Tokenizing String
tok_string = word_tokenize(string)

# Parts of Speech for the Tokenized String
pos_tok_string = pos_tag(tok_string)

# Creating Chunk Grammer
# NP - Noun Phrase, DT - Determiner, JJ - Adjective, NN - Noun

chunk_grammer = "NP:{<DT>?<JJ>*<NN>}"

# Creating Chunk Parser from above Created Chunk Grammer

chunk_parser = nltk.RegexpParser(chunk_grammer)

# Creating Tree from the Chunk Parser 

tree = chunk_parser.parse(pos_tok_string)

# Visually displaying the tree by draw method

tree.draw()