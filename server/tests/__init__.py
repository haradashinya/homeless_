#coding: utf-8

import models.db as db
from sqlalchemy.orm import scoped_session,sessionmaker
from models.score import Score
from models.user import User
from nose.tools import eq_,ok_

Session = sessionmaker(bind=db.engine)
session = Session()

db.drop_all()
db.init_db()

""" it should create user """
def test_create_user():
    user1 = User("nobinobi")
    user2 = User("foobar")
    session.add_all(user1,user2)
    session.commit()
    _user =  session.query(User).filter_by(name = "nobinobi").first()
    eq_(_user.name,"nobinobi")


