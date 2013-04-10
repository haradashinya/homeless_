#coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
engine = create_engine("sqlite:///app.db", convert_unicode = True,echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()



class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True)
    name = Column(String,unique=True)

    def __init__(self,name):
        self.name = name
        pass

    def commit(self):
        session.add(self)
        session.commit()

    def __repr__(self):
        return "<User('%s')>" % (self.name)


user = User("nobinobi")
user.commit()


# print session.query(User).filter_by(name="nobinobi").first().id


Base.metadata.create_all(engine)
