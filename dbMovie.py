import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
# client = MongoClient('')
# db = client.dbsparta
# cursor = db.collection.aggregate(
#     [
#         {"$group": {"_id": "$컬럼명", "unique_ids": {"$addToSet": "$_id"}, "count": {"$sum": 1}}},
#         {"$match": {"count": { "$gte": 2 }}}
#     ]
# )
# response = []
# for doc in list(cursor):
#     del doc["unique_ids"][0]
#     for id in doc["unique_ids"]:
#         response.append(id)

# movie = db.movies.find_one({'title':'가버나움'})
# star = movie['star']
#
# all_users = list(db.movies.find({'star':star}, {'_id':False}))
# for user in all_users:
#     print(user)


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
for song in songs:
    title = song.select_one('td.check > input.select-check').get('title')
    singer = song.select_one('td.info > a.artist').text
    rank = song.select_one('td.number').text[0:2].strip()
    print(rank, title, singer)

for song in songs:
    title = song.select_one('td.check > input.select-check').get('title')
    singer = song.select_one('td.info > a.artist').text
    rank = song.select_one('td.number').text[0:2].strip()
    print(rank, title, singer)
