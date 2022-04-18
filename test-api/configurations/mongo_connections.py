
from pymongo import MongoClient
from configurations.configuration_variables import MONGO_PORT

"mongodb://mongoadmin:mongoadmin@localhost:27017"
mongo_connection = MongoClient(port=int(MONGO_PORT))

print(mongo_connection)