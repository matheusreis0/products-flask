import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
import uuid
import datetime
Base = declarative_base()


def timestamp_now():
    return str(datetime.datetime.now())[:-7]


class BaseModel:

    __id = db.Column('id', db.String(length=36), primary_key=True, default=str(uuid.uuid4()))
    __created_at = db.Column('created_at', db.TIMESTAMP(), default=timestamp_now())
    __updated_at = db.Column('updated_at', db.TIMESTAMP(), default=timestamp_now())

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
