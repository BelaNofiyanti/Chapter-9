import requests

api_key ='e21fe8ee-0178-4356-8468-4b99d20262c3'
word ='potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)
    

    