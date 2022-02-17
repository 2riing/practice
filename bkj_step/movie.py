# import

from bs4 import BeautifulSoup
import requests
from pprint import pprint


# URL 및 요청 변수 
# https://developers.themoviedb.org/3/movies/get-movie-details
# https://api.themoviedb.org/3/movie/now_playing?api_key=bd2e2aed22ef7bc837f34ff1cf7ef434&region=KR%language=ko

BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/now_playing'
params = {
    'api_key' : 'bd2e2aed22ef7bc837f34ff1cf7ef434',
    'region' :'KR',
    'language' :'ko',
}

# 요청보낸 결과 저장

response = requests.get(BASE_URL+path, params=params)
print(response.status_code, response.url)
data = response.json()

# 조작 
# print(response)

# print(type(data)) # dict
# # print(data.keys()) # list
# print(type(data.get('results'))) # list
# print(data.get('results')[0]) # 영화정보 
# print(len(data.get('results'))) # 20 