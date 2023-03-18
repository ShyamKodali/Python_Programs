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

# Tokenizing String
tok_string = word_tokenize(string)

# Parts of Speech for the Tokenized String
pos_tok_string = pos_tag(tok_string)

# Creating Chunk Grammer with more than ONE Rule
# A grammar to determine what you want to include and exclude in our chunks
# {} - Rule that includes in the grammer; <.*>+ --> Includes Everything 
# }{ - Rule that excludes in the grammer

chink_chunk_grammar = """Chunk: {<.*>+}
                                }<JJ>{  """

# Creating Chunk Parser from above Created Chunk Grammer

chink_chunk_parser = nltk.RegexpParser(chink_chunk_grammar)

# Creating Tree from the Chunk Parser 

tree = chink_chunk_parser.parse(pos_tok_string)

# Creating Tree with NRE - Named Entity Recognistion  
tree1 = nltk.ne_chunk(pos_tok_string)

# Visually displaying the tree by draw method

tree.draw()
tree1.draw()