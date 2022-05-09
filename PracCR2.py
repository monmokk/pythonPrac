import json
import re

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://www.diffordsguide.com'
search_url = '/cocktails/search?include%5Bdg%5D=1&limit=20&sort=rating&offset=40'

# data = requests.get(url+search_url, headers=headers)
soup = BeautifulSoup(requests.get(url+search_url).text, 'html.parser')

cocktail_page = soup.find("script", {"type": "application/ld+json"})
# string_cocktail_page = cocktail_page.text  # HTML 요소 내 JSON으로 작성된 부분 문자열화
# dict_result = json.loads(string_cocktail_page)  # 문자열화한 결과를 다시 JSON으로 변환

print(cocktail_page)