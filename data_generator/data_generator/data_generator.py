import os
from unicodedata import category
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from faker import Faker
from pymysql import NULL

from postgresql_connection import Sql
from ecrypted import EncryiptionData
load_dotenv()

ROOT_DIR = os.path.dirname(os.path.abspath('')) 
DB_ENV = os.path.join(ROOT_DIR, '.env')

POSTGRE_USER = os.getenv('POSTGRE_USER')
POSTGRE_PASSWORD = os.getenv('POSTGRE_PASSWORD')
POSTGRE_HOST = os.getenv('POSTGRE_HOST')
POSTGRE_PORT = os.getenv('POSTGRE_PORT')
POSTGRE_DB_NAME = os.getenv('POSTGRE_DB_NAME')

MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_ROOT_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")


class DataGenerator:
    def __init__(self):
        self.sql = Sql()
        self.faker = Faker()
        self.encrypted = EncryiptionData()
        self.list_categories = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15"]
        self.list_names = ["b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9", "b10", "b11", "b12", "b13", "b14", "b15"]

    def user_data_generator(self, range_data):
        data_numeric_first = np.random.uniform(0, 1, range_data)
        data_numeric_second = np.random.uniform(-10, 10, range_data)
        data_numeric_third = np.random.uniform(10, 10000, range_data)
        data_numeric_fourth = np.random.randn(range_data)
        
        users_dataframe = pd.DataFrame({"data_numeric_1": data_numeric_first, "data_numeric_2": data_numeric_second, "data_numeric_third": data_numeric_third, "data_numeric_fourth": data_numeric_fourth, "data_size": range(range_data)})
        # data_save = self.sql.sql_append_data(users_dataframe, "userstest", )
        return users_dataframe

    def async_generator(self, range_data):
        list_names = []
        list_categories = []
        list_data_size = []
        for i in range(range_data):
            list_names.append(np.random.choice(self.list_names))
            list_categories.append(np.random.choice(self.list_categories))
            list_data_size.append(i)
        data_frame = pd.DataFrame({'categories': list_categories, 'names': list_names, 'id': list_data_size})
        self.sql.sql_db_save_data_table(data_frame, "asyncDataDemo")

        return data_frame


data_generator = DataGenerator()
frame_async_generator = data_generator.async_generator(500)

if __name__ == "__main__":
    print(frame_async_generator)