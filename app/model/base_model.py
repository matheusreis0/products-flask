import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
import uuid
import datetime
Base = declarative_base()


def timestamp_now():
    return str(datetime.datetime.now())[:-7]


def date_object(data):
    return {
        'hour': data.hour,
        'minute': data.minute,
        'second': data.second,
        'day': data.day,
        'month': data.month,
        'year': data.year,
        'timestamp': data.timestamp()
    }


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
    def created_at(self) -> dict:
        data = self.__created_at
        return date_object(data)

    @created_at.setter
    def created_at(self, created_at):
        self.__created_at = created_at

    @property
    def updated_at(self) -> dict:
        data = self.__updated_at
        return date_object(data)

    @updated_at.setter
    def updated_at(self, updated_at):
        self.__updated_at = updated_at
