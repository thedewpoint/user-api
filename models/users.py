
# https://realpython.com/python-sqlite-sqlalchemy/
# https://stackoverflow.com/questions/183042/how-can-i-use-uuids-in-sqlalchemy

from sqlalchemy import Column, Integer, String, ForeignKey, Table, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from .utils import Serializable

Base = declarative_base()

class Users(Base, Serializable):
    __tablename__ = "users"
    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()") )
    email = Column(String)
    zip = Column(String(5))
