import requests


url = '127.0.0.1'
data = {"password": 'pass',
        "login": 'login'}

respond = requests.get(url, params=data)
