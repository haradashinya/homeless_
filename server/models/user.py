#coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from base import Base

engine = create_engine("sqlite:///tmp/app.db", convert_unicode = True)



class User(Base):
    def __init__(self):
        Base.__init__(self)
        self.hello()

    def create(self):
        print "called create"
        pass
