import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8392af2fdfc76bd54e7354c14cf8104c'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '18360'
TRAINER_NAME = 'Паша Техник'


'''Проверяем Get/trainers в ответе Статус код 200'''

def test_status_codeTR():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id':TRAINER_ID})
    assert response.status_code == 200
 
'''Проверяем наличие ключа trainer_name со значением Паша Техник'''

def test_trainer_name():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id':TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Паша Техник'

    
'''Проверка параметров тренера таких как: имя тренера, уровень, город'''

@pytest.mark.parametrize('key, value', [('trainer_name','Паша Техник'), ('level', '1'), ('city','Алупка')])
def test_parametrizeTRAINER(key, value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()['data'][0][key] == value

'''Проверяем Get/pokemons в ответе Статус код 200'''

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id':TRAINER_ID})
    assert response.status_code == 200

'''Проверяем наличие ключа name со значением Чикенкари'''

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id':TRAINER_ID})
    assert response_get.json()['data'][0]['name'] == 'Чикенкари'

'''Проверка параметров покемона таких как: имя покемона, айди тренера, айди покемона'''

@pytest.mark.parametrize('key, value', [('name','Чикенкари'), ('trainer_id', TRAINER_ID), ('id','223248')])
def test_parametrizePOKEMON(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()['data'][0][key] == value


