from pymongo import MongoClient
import pandas as pd
import random

class MongoDB(object):
    def __init__(self, host='localhost', port=27017, database_name="mockupdata", collection_name="QH_S1"):
        try:
            self._connection = MongoClient(username="TGR_GROUP16", password="ED370J", host=host, port=port, maxPoolSize=200)
        except Exception as error:
            raise Exception(error)
        self._database = None
        self._collection = None
        if database_name:
            self._database = self._connection[database_name]
        if collection_name:
            self._collection = self._database[collection_name]

    def insert(self, post):
        # add/append/new single record
        post_id = self._collection.insert_one(post).inserted_id
        return post_id

print('[*] Pushing data to MongoDB ')
mongo_db = MongoDB()

df = pd.read_csv("E:/extra/TGR2023/dataset8/QH_S1.csv")
dataframe = pd.DataFrame(data = df, )

for collection in dataframe:
    print('[!] Inserting - ', collection)
    mongo_db.insert(collection)