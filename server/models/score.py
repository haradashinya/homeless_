#coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship, backref
import db


class Score(db.Base):
    __tablename__ = "scores"
    id = Column(Integer,primary_key=True)
    point = Column(Integer)
    user_id = Column(Integer,ForeignKey('users.id'))

    def __init__(self,point):
        self.point = int(point)

