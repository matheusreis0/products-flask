import sqlalchemy as db
from sqlalchemy.orm.session import sessionmaker

class BaseDao:

    def __init__(self):
        pass

    def __get_connection(self):
        pass

    def read(self, id: str = ''):
        pass
    
    def insert(self, model):
        pass

    def update(self, model):
        pass

    def delete(self, id):
        pass
