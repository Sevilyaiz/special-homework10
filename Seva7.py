import requests

params = {'q' : 'видео'}

responce = requests.get('https://www.youtube.com/live/dQz3SAbuHy8/search',params=params)
print(responce.status_code)
print(responce.headers)
print(responce.text)

Api_token = 'a6d3166dd8cc41cd297dba0ee32dcfad'

import requests
from apikey import API_TOKEN
params = {'q' : 'Лондон', 'appid': API_TOKEN,'units': 'metric'}

responce = requests.get('https://api.openweathermap.org/data/2.5/weather',params=params)
# print(responce.status_code)
# print(responce.headers)
# print(responce.text)
