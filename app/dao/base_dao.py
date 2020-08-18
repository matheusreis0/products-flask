import sqlalchemy as db
from sqlalchemy.orm.session import sessionmaker


class BaseDao:

    def __init__(self, model_class):
        self.__connector = ''
        self.__hostname = ''
        self.__username = ''
        self.__password = ''
        self.__database = ''
        self.__get_connection()
        self.__model_class = model_class

    def __get_connection(self):
        engine = db.create_engine(
            f'{self.__connector}://{self.__username}:{self.__password}@{self.__hostname}/{self.__database}'
        )
        Session = db.orm.sessionmaker()
        Session.configure(bind=engine)
        self.__session = Session()

    def read(self, id: str = ''):
        pass

    def insert(self, model):
        pass

    def update(self, model):
        pass

    def delete(self, id):
        pass