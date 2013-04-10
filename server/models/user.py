#coding: utf-8
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship, backref
import db


# init data bases.
db.drop_all()


Session = sessionmaker(bind=db.engine)
session = Session()


class Score(db.Base):
    __tablename__ = "scores"
    id = Column(Integer,primary_key=True)
    point = Column(Integer)
    user_id = Column(Integer,ForeignKey('users.id'))

    def __init__(self,point):
        self.point = int(point)



class User(db.Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    scores = relationship("Score",backref="user")

    def __init__(self,name):
        self.name = name
        pass


    def __repr__(self):

        return "<User('%s')>" % (self.name)

    def push_to_score(self,point):
        self.scores.append(Score(point))

    # return all scores.
    def all_scores():
        pass

    # return high score of the user.
    def high_score(self):
        res = []
        for score in self.scores:
            res.append(score.point)
        high =  [arr for arr in sorted(res)][len(res) -1]
        print "log: high: %i " % high
        return high

db.init_db()

# create user
user = User("nobinobi")

user.push_to_score(10)
user.push_to_score(10)
user.push_to_score(15)
user.push_to_score(30)
user.high_score()


session.add(user)
session.commit()




# for user in session.query(User).all():
#     for score in user.scores:
#         print score.point



