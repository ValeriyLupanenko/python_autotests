import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8392af2fdfc76bd54e7354c14cf8104c'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "super.valeriylu@yandex.ru",
    "password": "QA2024"
}

body_create = {
    "name": "Бигтейсти",
    "photo_id": 1
}

body_put = {
    "pokemon_id": "223248",
    "name": "Чикенкари",
    "photo_id": 1
}

body_pokeball = {
    "pokemon_id": "223248"
}

'''Получаем код 400 с текстом Такой тренер уже существует'''
'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_put = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_put)
print(response_put.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)