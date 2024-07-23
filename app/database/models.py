from sqlalchemy import Column, ForeignKey, Integer, String, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    __tableargs__ = {"comment": "Table with users of app"}

    id = Column(
        Integer, nullable=False, unique=True, primary_key=True, autoincrement=True
    )
    login = Column(String(128),
                   unique = True, 
                   nullable=False)
    password_hash = Column(String(128))
    
    
    
class Tokens(Base):
    __tablename__="tokens"
    __tableargs__={"comment":"Table with user refresh tokens"}
    id = Column(Integer,
                unique=True,
                nullable=False,
                autoincrement=True, 
                primary_key=True)
    refresh_token = Column(Text, 
                               unique=True,
                               nullable = False)
    user_id = Column(Integer,
                     ForeignKey("users.id"))
    
class Task(Base):
    __tablename__="tasks"
    __tableargs__={"comment":"Table with notes of users"}
    
    id = Column(Integer, 
                unique = True,
                autoincrement=True, 
                primary_key=True,
                nullable=False)
    user_id=Column(Integer,
                   ForeignKey("users.id"))
    task=Column(Text, 
                unique=False)