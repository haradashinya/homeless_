#coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship, backref

engine = create_engine("sqlite:///app.db", convert_unicode = True,echo=True)
Base = declarative_base()



def init_db():
    Base.metadata.create_all(engine)

def drop_all():
    print "drop"
    Base.metadata.drop_all(engine)








