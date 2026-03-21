from pymongo import MongoClient
from fastAPITest.src.model import blogModel
from typing import List
from pydantic import TypeAdapter

connection = MongoClient("mongodb://localhost")

db = connection.test

cursor = db.blog.find()
# blogsArray = []
# for d in cursor:
#     blogsArray.append(d)

# print(blogsArray)

blogListAdapter = TypeAdapter(List[blogModel.BlogModel])
validated_list = blogListAdapter.validate_python(cursor)
print(validated_list)