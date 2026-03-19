from pymongo import MongoClient

connection = MongoClient("mongodb://localhost")

db = connection.test

cursor = db.blog.find()
for d in cursor:
    print(d)