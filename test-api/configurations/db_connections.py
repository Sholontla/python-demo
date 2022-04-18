import pandas as pd
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column
from configurations.configuration_variables import POSTGRE_USER, POSTGRE_PASSWORD, POSTGRE_HOST, POSTGRE_PORT, POSTGRE_DB_NAME

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine(f"postgresql+psycopg2://{POSTGRE_USER}:{POSTGRE_PASSWORD}@{POSTGRE_HOST}:{POSTGRE_PORT}/{POSTGRE_DB_NAME}", echo=False)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Sql:
    def __init__(self):
        self.engine_postgres_sqlalchemy = create_engine(f"postgresql+psycopg2://{POSTGRE_USER}:{POSTGRE_PASSWORD}@{POSTGRE_HOST}:{POSTGRE_PORT}/{POSTGRE_DB_NAME}", echo=False)
    def sql_db_read_tables(self):
        Session = sessionmaker(bind=self.engine_postgres_sqlalchemy)
        session = Session()
        conn = self.engine_postgres_sqlalchemy.connect()
        db_nombres = self.engine_postgres_sqlalchemy.table_names()
        db_nombres_df = pd.DataFrame(db_nombres, columns=["db_nombres"])
        return db_nombres_df

    def sql_db_save_data_table(self, sql_table_name=None):
        data_frame = pd.DataFrame()
        data_save = data_frame.to_sql(sql_table_name, self.engine_postgres_sqlalchemy)
        data_save = self.engine_postgres_sqlalchemy.execute(f"SELECT * FROM {sql_table_name}").fetchall()

    def sql_db_read_table(self, dataframe_name):
        pd.options.display.max_columns=None
        df_sql = pd.read_sql_table(dataframe_name, self.engine_postgres_sqlalchemy)
        df = pd.DataFrame(df_sql)
        return df

    def sql_db_replace_data(self, df, tableName):
        data = df.to_sql(f'{tableName}', con=self.engine_postgres_sqlalchemy, if_exists='replace', index_label='id')
        data = self.engine_postgres_sqlalchemy.execute(f"SELECT * FROM {tableName}").fetchall()
        return data

    def sql_append_data(self, df, tableName):
        df.to_sql(f'{tableName}', con=self.engine_postgres_sqlalchemy, if_exists='append', index_label='id')
        return self.engine_postgres_sqlalchemy.execute(f"SELECT * FROM {tableName}").fetchall()

# SQL = Sql()
# db_pandas = SQL.sql_db_read_table("users_blog")
# print(db_pandas)



