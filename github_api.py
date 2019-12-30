# У гитхаба есть публичное API. Создай тест для коллбека, который возвращает репозитории пользователя.
# Проверь, что этот коллбек возвращает твой репозиторий в ответе.
# Используй питон и библиотеку requests.

import requests
from requests.exceptions import HTTPError

url = 'https://api.github.com'
g = '/users/Ikivas/repos'

response = requests.get(url + g)
response.raise_for_status()

name = 'QA'
data = response.json()

def check_data():
    for item in data:
        if item['name'] == 'QA':
            print('Success!')
            return
    raise ValueError("No target in given data")

check_data()
