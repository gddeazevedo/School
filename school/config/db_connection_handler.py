from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    '''Class to handle the connection with the database'''
    def __init__(self):
        self.__engine = create_engine('mysql+pymysql://root:1234@localhost:3306/school')
        self.__session = None

    @property
    def engine(self):
        return self.__engine

    @property
    def session(self):
        return self.__session

    def __enter__(self):
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__session.close()

