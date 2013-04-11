# coding: utf-8


from sqlalchemy.orm import scoped_session,sessionmaker
from nose.tools import eq_
import models.db as db
from models.user import User
from models.score import Score
# create user
# user = User("nobinobi")
#
# user.push_to_score(10)
# user.push_to_score(10)
# user.push_to_score(15)
# user.push_to_score(30)
# user.push_to_score(50)
# user.push_to_score(55)
# user.high_score()
#
# session.add(user)
# session.commit()

Session = sessionmaker(bind=db.engine)
session = Session()


""" it should create user """
def test_create_user():
    user1 = User("nobinobi")
    user2 = User("foo")
    session.add(user1)
    session.add(user2)
    session.commit()
    u = session.query(User).filter_by(name = "nobinobi").first()
    _user =  session.query(User).filter_by(name = "nobinobi").first()
    eq_(u.name,"nobinobi")


def test_report_score():
    pass



