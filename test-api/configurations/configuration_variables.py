import os
from dotenv import load_dotenv

load_dotenv()

ROOT_DIR = os.path.dirname(os.path.abspath('')) 
DB_ENV = os.path.join(ROOT_DIR, '.env')

POSTGRE_USER = os.getenv('POSTGRE_USER')
POSTGRE_PASSWORD = os.getenv('POSTGRE_PASSWORD')
POSTGRE_HOST = os.getenv('POSTGRE_HOST')
POSTGRE_PORT = os.getenv('POSTGRE_PORT')
POSTGRE_DB_NAME = os.getenv('POSTGRE_DB_NAME')

MONGO_PORT = os.getenv('MONGO_PORT')
MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_ADMIN_USER = os.getenv('MONGO_ADMIN_USER')
MONGO_ADMIN_PASSWORD = os.getenv('MONGO_ADMIN_PASSWORD')

API_SERVER_PORT = os.getenv('API_SERVER_PORT')
API_SERVER_HOST = os.getenv('API_SERVER_HOST')

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
