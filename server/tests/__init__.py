#coding: utf-8

import models.db as db
from sqlalchemy.orm import scoped_session,sessionmaker
from models.score import Score
from models.user import User
from nose.tools import eq_,ok_
db.drop_all()
db.init_db()

Session = sessionmaker(bind=db.engine)
session = Session()




