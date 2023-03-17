import nltk

string = """A latte is a milk coffee that is a made up of one or two shots of espresso, steamed milk and a final, thin layer of frothed milk on top. 
            If you don't drink dairy milk, you can easily swap it for a plant-based alternative like soy, oat or coconut milk.
            The origins of the latte aren’t very clear as people have been combining coffee and milk for centuries. 
            However, the silky beverage that we know and love today is thought to originate in America, hitting the peak of popularity in Seattle during the 80’s."""
            
# Tokenizing by sentence 

Tok_by_Sent = nltk.sent_tokenize(string)
print(Tok_by_Sent)
print('*************************************************************************************************************')

# Tokenizing by word 

Tok_by_Word = nltk.word_tokenize(string)
print(Tok_by_Word)