import pandas as pd
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column
import os
from dotenv import load_dotenv

from sqlalchemy.orm import scoped_session, sessionmaker
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

MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_ROOT_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

class Sql:
    def __init__(self):
        self.postgre = create_engine(f"postgresql+psycopg2://{POSTGRE_USER}:{POSTGRE_PASSWORD}@{POSTGRE_HOST}:{POSTGRE_PORT}/{POSTGRE_DB_NAME}", echo=False)
        # self.mysql = create_engine(f'mysql+pymysql://{MYSQL_USER}:{MYSQL_ROOT_PASSWORD}@localhost/{MYSQL_DATABASE}')
        # self.engine = create_engine('mssql+pyodbc://localhost:1433@mydsn')

    def sql_db_read_tables(self):
        Session = sessionmaker(bind=self.postgre)
        session = Session()
        conn = self.postgre.connect()
        db_nombres = self.postgre.table_names()
        db_nombres_df = pd.DataFrame(db_nombres, columns=["db_nombres"])
        return db_nombres_df

    def sql_db_save_data_table(self, data_frame, sql_table_name):
        data_save = data_frame.to_sql(f"{sql_table_name}", self.postgre)
        data_save = self.postgre.execute(f"SELECT * FROM {sql_table_name}").fetchall()
        return data_save

    def sql_db_read_table(self, dataframe_name):
        df_sql = pd.read_sql_table(dataframe_name, self.postgre)
        df = pd.DataFrame(df_sql)
        return df

    def sql_db_replace_data(self, df, tableName, engine):
        data = df.to_sql(f'{tableName}', con=engine, if_exists='replace', index_label='id')
        data = engine.execute(f"SELECT * FROM {tableName}").fetchall()
        return data

    def sql_append_data(self, df, tableName):
        df.to_sql(f'{tableName}', con=self.postgre, if_exists='append', index_label='columns')
        return self.postgre.execute(f"SELECT * FROM {tableName}").fetchall()



SQL = Sql()
db_pandas = SQL.sql_db_read_table("asyncDataDemo")
print(db_pandas)

