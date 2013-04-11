# coding: utf-8

from nose.tools import eq_
import models.db as db
from models.user import User
from models.score import Score

# db.drop_all()
# db.init_db()

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

class TestDB(object):
    def setup(self):
        print "hello"





