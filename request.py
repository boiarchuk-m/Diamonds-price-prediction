import requests

url = f'http://localhost:9696/predict'


diamond = {'shape': 'Round', 'carat':0.30, 'cut': 'Very Good', 'color': 'I', 'clarity': 'VS1',
             'report': 'GIA', 'type': 'natural'}

response = requests.post(url, json=diamond).json()
print(response)
