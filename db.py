from sqlalchemy import create_engine, text, func, MetaData
from sqlalchemy.orm import declarative_base, Mapped, sessionmaker, mapped_column
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.schema import UniqueConstraint

from contextlib import contextmanager

import os
from dotenv import load_dotenv

import pandas as pd

from utils.errors.errors import NotFoundError
from utils.logger import Logger

load_dotenv()

POSTGRE_USER = os.getenv('POSTGRE_USER')
POSTGRE_PASSWORD = os.getenv('POSTGRE_PASSWORD')
POSTGRE_HOST = os.getenv('POSTGRE_HOST')
POSTGRE_PORT = os.getenv('POSTGRE_PORT')
POSTGRE_DB_NAME = os.getenv('POSTGRE_DB_NAME')

DeclarativeBase = declarative_base()


def log(logger):
    def decorator(func):
        def wrapper(*args, **kwargs):
            logger.info("Starting execution of function: %s" %
                        func.__name__)
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                logger.error(
                    "Error occurred while executing function %s: %s" % (func.__name__, e))
                raise
            logger.info("Completed execution of function: %s" %
                        func.__name__)
            return result
        return wrapper
    return decorator


info_logger = Logger.get_info_logger("info_logger")
error_logger = Logger.get_error_logger("error_logger")


@contextmanager
def SQLPostgresContext():
    try:
        db = SQLPostgres()
        yield db
    finally:
        db.session.close()


class SQLPostgres:
    def __init__(self):
        self.engine = create_engine(
            f"postgresql+psycopg2://{POSTGRE_USER}:{POSTGRE_PASSWORD}@{POSTGRE_HOST}:{POSTGRE_PORT}/{POSTGRE_DB_NAME}", echo=False)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.metadata = MetaData()

    def migrations(self):
        DeclarativeBase.metadata.create_all(self.engine)

    def sql_read_tables(self):
        metadata = MetaData()
        metadata.reflect(bind=self.engine)
        table_names = metadata.tables.keys()
        db_nombres_df = pd.DataFrame(table_names, columns=["db_nombres"])
        return db_nombres_df

    def insert_data(self, data):
        # Query the max ID value
        max_id = self.session.query(func.max(Customers.id)).scalar()

        # Set the ID value for the new record
        if max_id is None:
            data.id = 1
        else:
            data.id = max_id + 1

        try:
            self.session.add(data)
            self.session.commit()
            return data

        except IntegrityError:
            self.session.rollback()
            return "Data already exists"

    def instert_multiple_data(self, data=list):
        self.session.add_all(data)
        self.session.commit()

    def get_record(self, data):
        self.session.add(data)
        self.session.commit()

    def get_all_records(self):
        query = text("SELECT username, useremail FROM customers")
        result = self.session.execute(query)
        rows = [dict(username=row[0], useremail=row[1]) for row in result]
        return rows

    def get_filter_record_sql(self, column_value):
        query = text(
            f"SELECT id, username, useremail FROM {Customers.__tablename__} WHERE username = :value"
        ).bindparams(value=column_value)
        table_class = Customers
        result = self.session.execute(query).fetchone()

        if result:
            # Get the column names from the table definition of the SQLAlchemy model
            columns = [
                column.name for column in table_class.__table__.columns]
            # Convert the tuple into a dictionary with column names as keys
            return {column: value for column, value in zip(columns, result)}
        else:
            error_logger.error(f"Could not find: {NoResultFound}")
            raise NotFoundError()

    def updated_record(self, table_class, column_name, column_value):
        filter_condition = getattr(table_class, column_name) == column_value
        result = self.session.query(table_class).filter(
            filter_condition).first()
        try:
            return {key: value for key, value in result.__dict__.items() if not key.startswith('_')}
        except:
            raise NotFoundError({"error": "record dont exist"})


class Customers(DeclarativeBase):
    __tablename__ = 'customers'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=True, unique=True)
    useremail: Mapped[str] = mapped_column(nullable=True, unique=True)
    __table_args__ = (UniqueConstraint('username', 'useremail'),)


# class Order(Base):
#     __tablename__ = 'order'
#     id:Mapped[int] = mapped_column(primiary_key=True)
#     store:Mapped[str] = mapped_column(nullable=True)
#     products:Mapped[str] = mapped_column(nullable=True)
#     quantity:Mapped[int] = mapped_column(nullable=True)
#     customer_id:Mapped[int] = mapped_column(ForeignKey("customers.id"))


# class Store(Base):
#     __tablename__ = 'store'
#     id:Mapped[int] = mapped_column(primiary_key=True)
#     sotre_reference:Mapped[str] = mapped_column(nullable=True)
#     store_email:Mapped[str] = mapped_column(nullable=True)
#     store_manager:Mapped[str] = mapped_column(nullable=True)


# class Producrs(Base):
#     __tablename__ = 'products'
#     id:Mapped[int] = mapped_column(primiary_key=True)
#     category:Mapped[str] = mapped_column(nullable=True)
#     sub_category:Mapped[str] = mapped_column(nullable=True)
#     product:Mapped[str] = mapped_column(nullable=True)
#     price:Mapped[float] = mapped_column(nullable=True)


sql = SQLPostgres()

print(sql.migrations())
# print(sql.sql_read_tables())

# sql.insert_data(Customers(username="thom", useremail="thom@example.com"))
# print(sql.get_all_records())
# print(sql.get_filter_record_sql(Customers, 'username', 'thom'))
