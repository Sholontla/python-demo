import time
import pandas as pd
import numpy as np
from datetime import datetime

from data_connections.mongo_connections import  MongoConnection

from data_generator.data_sales_generator import SalesDataGenerator

class Generator:
    def __init__(self, seconds):
        self.SalesDataGenerator = SalesDataGenerator(seconds)
        self.mongo_class = MongoConnection()
        self.SalesDataGenerator = SalesDataGenerator(seconds)

    def generate_users(self):
        user_data_generator = []
        for i in self.SalesDataGenerator.user_generator():
            dict_i = i.dict()
            user_data_generator.append(dict_i)
            print(dict_i)
            self.mongo_class.add_elements_collection(i.dict())

    def generate_users_interactions(self):
        user_data_generator = []
        print(self.SalesDataGenerator.user_interaction_generator())
            # self.mongo_class.add_elements_collection(i.dict())


    def category_generator(self):
        self.SalesDataGenerator.product_category_generator()
    
    def inventory_generator(self):
        self.SalesDataGenerator.product_inventory_generator()

    def generator_discount(self):
        self.SalesDataGenerator.discount_generator()
    


    
