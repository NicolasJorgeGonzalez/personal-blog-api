from pymongo import MongoClient

client = MongoClient("mongo://localhost/27017")
db     = client["blog-api"]