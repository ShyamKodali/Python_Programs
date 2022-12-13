def str2emj(string):
    emoji_dict = {
        'laugh' : '😂',
        'lol' : '🤣',
        'tease laugh' : '😜',
        'cry' : '😭',
        'love' : '💘',
        'sad' : '😞',
        'kiss' : '😘',
        'hug' : '🤗',
        'happy' : '😁'}
    words = message.split(" ")
    res = ""
    for word in words:
        res += emoji_dict.get(word, word) + " "
    return res 


message = input(str('Enter your statement to convert into emojis: '))
print(str2emj(message))
