import requests as re

url = 'https://realpython.com/python-requests/'
f = re.get(url)

# Prints text format of the web page
print(f.text)
print('**************************************************************************************************************')


h = re.head(url)
# Prints headers 
print(h.headers)