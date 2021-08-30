from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.sql.sqltypes import PickleType
from user_app.models.user_models import BaseModel

DB_NAME = 'fast_api'


class DBResource:
    def __init__(
        self, username: str='danish', password: str='root', host: str='localhost', port: int=3306, db_name: str=DB_NAME
        ):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        

    def get_db_engine(self, db_name: str=DB_NAME):
        DB_URL = f"mysql+pymysql://{self.username}:{self.password}@{self.host}:{self.port}/{db_name}"
        return create_engine(DB_URL)
    
    def get_db_connection(self, db_name: str=DB_NAME):
        engine = self.get_db_engine(db_name=db_name)
        return engine.connect()

    def get_db_session(self, db_name: str=DB_NAME):
        engine = self.get_db_engine(db_name)
        return self.get_db_session_from_engine(engine=engine)

    def create_database(self, db_name: str=DB_NAME):
        engine = self.get_db_engine(db_name=db_name)
        print(engine, '...engine create database')
        return engine.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    
    @staticmethod
    def get_db_session_from_engine(engine: create_engine) -> Session:
        return Session(bind=engine)

    def create_all_tables(self, db_name: str=DB_NAME):
        engine = self.get_db_engine(db_name=db_name)
        BaseModel.metadata.create_all(engine)



if __name__ == '__main__':
    db = DBResource()
    db.create_all_tables()