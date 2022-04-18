from typing import Dict
from pymongo import MongoClient


class MongoConnection:
    def __init__(self):
        cliente = "mongodb://testingmongo:testingmongo@localhost:27017"
        self.client = MongoClient(cliente)
        self.db = self.client['test']
        self.collection_data_producer = self.db['data-vault']
        self.collection_data_interaction = self.db['UsersInteraction']

    def connections(self):
        databeses = self.client.list_database_names()
        list_collections = self.db.list_collection_names()
        documnets_count = self.collection_data_interaction.count_documents({})
        self.collection_data_producer.count_documents({})
        print(list_collections)
        print("Collection List: ", documnets_count, " - ", self.collection_data_producer.count_documents({}))

    def add_elements_collection(self, data):
        self.collection_data_producer.insert_one(
            data
        )

    def add_many_elements_user_producer_collection(self, data):
        self.collection_data_producer.insert_many([
            data
        ])

    def add_many_elements_user_interation_collection(self, data):
        self.collection_data_interaction.insert_many([
            data
        ])


    def data_find_elements_user_producer_collection(self):
        # for i in self.collection.find():
        #     print(i)
        data = [i for i in self.collection_data_producer.find()]
        return data

    def data_find_elements_user_interaction_collection(self):
        # for i in self.collection.find():
        #     yield i
        data = [i for i in self.collection_data_interaction.find()]
        return data


    def data_find_by_id(self):
        return self.collection.find_one("title")

print(MongoConnection().data_find_elements_user_producer_collection())
