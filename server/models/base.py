#coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine("sqlite:///tmp/app.db", convert_unicode = True)

class BaseModel:
    def __init__(self):
        print "called base"
        pass

    def hello(self):
        print "hello called"
