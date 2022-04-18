import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


load_dotenv()

ROOT_DIR = os.path.dirname(os.path.abspath('')) 
DB_ENV = os.path.join(ROOT_DIR, '.env')

POSTGRE_USER = os.getenv('POSTGRE_USER')
POSTGRE_PASSWORD = os.getenv('POSTGRE_PASSWORD')
POSTGRE_HOST = os.getenv('POSTGRE_HOST')
POSTGRE_PORT = os.getenv('POSTGRE_PORT')
POSTGRE_DB_NAME = os.getenv('POSTGRE_DB_NAME')

ENCRYPTED_POSTGRE_USER =  os.getenv('ENCRYPTED_POSTGRE_USER')
ENCRYPTED_POSTGRE_PASSWORD =  os.getenv('ENCRYPTED_POSTGRE_PASSWORD')
ENCRYPTED_POSTGRE_HOST = os.getenv('ENCRYPTED_POSTGRE_HOST')
ENCRYPTED_POSTGRE_PORT = os.getenv('ENCRYPTED_POSTGRE_PORT')
ENCRYPTED_POSTGRE_DB_NAME = os.getenv('ENCRYPTED_POSTGRE_DB_NAME')  

class Sql:
    def __init__(self):
        self.engine_postgres_sqlalchemy = create_engine(f"postgresql+psycopg2://{POSTGRE_USER}:{POSTGRE_PASSWORD}@{POSTGRE_HOST}:{POSTGRE_PORT}/{POSTGRE_DB_NAME}", echo=False)
        self.engine_postgres_sqlalchemy_encrypted = create_engine(f"postgresql+psycopg2://{ENCRYPTED_POSTGRE_USER}:{ENCRYPTED_POSTGRE_PASSWORD}@{ENCRYPTED_POSTGRE_HOST}:{ENCRYPTED_POSTGRE_PORT}/{ENCRYPTED_POSTGRE_DB_NAME}", echo=False)

    def sql_db_read_tables(self):
        Session = sessionmaker(bind=self.engine_postgres_sqlalchemy)
        session = Session()
        conn = self.engine_postgres_sqlalchemy.connect()
        db_nombres = self.engine_postgres_sqlalchemy.table_names()
        db_nombres_df = pd.DataFrame(db_nombres, columns=["db_nombres"])
        return db_nombres_df

    def sql_db_save_data_table(self, dataframe, sql_table_name):
        data_save = dataframe.to_sql(f"{sql_table_name}", self.engine_postgres_sqlalchemy)
        data_save = self.engine_postgres_sqlalchemy.execute(f"SELECT * FROM {sql_table_name}").fetchall()
        return data_save

    def sql_db_read_table(self, dataframe):
        df_sql = pd.read_sql_table(dataframe, self.engine_postgres_sqlalchemy)
        df = pd.DataFrame(df_sql)
        return df

    def sql_db_replace_data(self, dataframe, table_name):
        data = dataframe.to_sql(f'{table_name}', con=self.engine_postgres_sqlalchemy, if_exists='replace', index_label='id')
        data = self.engine_postgres_sqlalchemy.execute(f"SELECT * FROM {table_name}").fetchall()
        return data

    def sql_append_data(self, dataframe, table_name):
        dataframe.to_sql(f'{table_name}', con=self.engine_postgres_sqlalchemy, if_exists='append', index_label='columns')
        return self.engine_postgres_sqlalchemy.execute(f"SELECT * FROM {table_name}").fetchall()

# SQL = Sql()
# db_pandas = SQL.sql_db_read_table("interaction_users")




