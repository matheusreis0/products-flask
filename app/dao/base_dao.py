from sqlalchemy import exc
import sqlalchemy as db
from sqlalchemy.orm.session import sessionmaker


class BaseDao:

    def __init__(self, model_class):
        self.__connector = 'mysql+mysqlconnector'
        self.__hostname = 'mysql.padawans.dev'
        self.__username = 'padawans02'
        self.__password = 'ote2020'
        self.__database = 'padawans02'
        self.__get_connection()
        self.__model_class = model_class

    def __get_connection(self):
        engine = db.create_engine(
            f'{self.__connector}://{self.__username}:{self.__password}@{self.__hostname}/{self.__database}'
        )
        Session = db.orm.sessionmaker()
        Session.configure(bind=engine)
        self.__session = Session()

    def __read_one(self, id: str):
        model = self.__session.query(self.__model_class).get(id)
        if model:
            return model
        return {}

    def read(self, id: str = ''):
        if id:
            return self.__read_one(id)
        rows = self.__session.query(self.__model_class).all()
        return rows

    def insert(self, model):
        self.__session.add(model)
        if self.__try_commit():
            return model
        return {'success': False}

    def update(self, model):
        if not type(self.__read_one(model.id)) == dict:
            self.__session.merge(model)
            if self.__try_commit():
                return self.__read_one(model.id)
        return {'success': False}

    def delete(self, id):
        model = self.read(id)
        if not type(model) == dict:
            self.__session.delete(model)
            if self.__try_commit():
                return {'success': True}
        return {'success': False}

    def __try_commit(self) -> bool:
        try:
            self.__session.commit()
            return True
        except exc.SQLAlchemyError:
            return False
