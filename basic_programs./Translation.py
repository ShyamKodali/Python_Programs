def translate(phrase):
    translation = ""
    
    for letter in phrase:
        if letter.lower()in "aeiou":
            if letter.isupper():
                translation = translation + "J"
            else:
                translation = translation + 'j'
        else:
            translation = translation + letter
    return translation
            
print(translate(input("Enter a phrase to transalte in J/j Language: ")))
