### Ahmad Riyadh Al Faathin - 155150207111052 - SKT C - Faathin.com ###
# Import library pymongo
from pymongo import MongoClient

class DatabaseHandler:
    
    client = object
    db = object

    def __init__(self, host, port, database):
        self.client = MongoClient(host, port)
        self.db = self.client[database]

    def getCollection(self, collection):
        return self.db[collection]

    def insertOneDocument(self, collection, data):
        c = self.getCollection(collection)
        return c.insert_one(data)

    def findOneDocument(self, collection, data):
        c = self.getCollection(collection)
        return c.find_one(data)

    def insertBulkDocument(self, collection, data):
        c = self.getCollection(collection)
        return c.insert_many(data)

    def findBulkDocument(self, collection, data):
        c = self.getCollection(collection)
        return c.find(data)
