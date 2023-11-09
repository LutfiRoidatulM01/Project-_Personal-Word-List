import requests

api_key = '1ebd433e-b6cc-4d6f-8a13-cbb50986952a'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)

# root_url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json'
# final_url = f'{root_url}/{word}?key={api_key}'
# r = requests.get(final_url)
# result = r.json()
# print(result)