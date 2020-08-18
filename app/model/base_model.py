import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class BaseModel:

    __id = db.Column('id', db.String(length=36), primary_key=True)
    __created_at = db.Column('created_at', db.TIMESTAMP())
    __updated_at = db.Column('updated_at', db.TIMESTAMP())

    def __init__(self, id: str = '', created_at:str = '', updated_at: str = ''):
        self.__id = id
        self.__created_at = created_at
        self.__updated_at = updated_at

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def created_at(self) -> str:
        return self.__created_at

    @created_at.setter
    def created_at(self, created_at):
        self.__created_at = created_at

    @property
    def updated_at(self) -> str:
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        self.__updated_at = updated_at
