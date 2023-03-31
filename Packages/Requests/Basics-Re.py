import requests as re

url = 'https://realpython.com/python-requests/'
response = re.get(url)

# Prints text format of the web page
print(response.text)
print('**************************************************************************************************************')

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')

print('**************************************************************************************************************')


h = re.head(url)
# Prints headers 
print(h.headers)