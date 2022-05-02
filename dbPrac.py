from pymongo import MongoClient
client = MongoClient('')
db = client.dbsparta

doc = {
    'name' : 'mj',
    'age' : 32
}

# db.users.insert_one({'name':'jj', 'age':33})

all_users = list(db.users.find({},{'_id':False}))

# for user in all_users:
#     print(user)

user = db.users.find_one({'name':'mj'}, {'_id':False})
# print(user)

db.users.update_one({'name':'mj'},{'$set':{'age':20}})

# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
all_users = list(db.users.find({},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})