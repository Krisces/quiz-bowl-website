from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    data=db.Column(db.String(10000))
    date=db.Column(db.DateTime(timezone=True), default=func.now())
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))     #One-to-many-relationship


#Database model for users. Saves unique id and email, as well as password and first name
class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(150), unique=True)
    password=db.Column(db.String(150))
    first_name=db.Column(db.String(150))
    notes=db.relationship('Note')

class Topic(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50))

class Geocard(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    question=db.Column(db.String(1000))
    answer=db.Column(db.String(100))

class Historycard(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    question=db.Column(db.String(1000))
    answer=db.Column(db.String(100))   
    
class Literaturecard(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    question=db.Column(db.String(1000))
    answer=db.Column(db.String(100))

class Mathematicscard(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    question=db.Column(db.String(1000))
    answer=db.Column(db.String(100))

class Miscellaneouscard(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    question=db.Column(db.String(1000))
    answer=db.Column(db.String(100))

class Musicandauditoryartcard(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    question=db.Column(db.String(1000))
    answer=db.Column(db.String(100))

class Mythologycard(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    question=db.Column(db.String(1000))
    answer=db.Column(db.String(100))

class Peoplecard(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    question=db.Column(db.String(1000))
    answer=db.Column(db.String(100))

class Performancecard(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    question=db.Column(db.String(1000))
    answer=db.Column(db.String(100))   

class Philosophycard(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    question=db.Column(db.String(1000))
    answer=db.Column(db.String(100))

class Popularculturecard(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    question=db.Column(db.String(1000))
    answer=db.Column(db.String(100))

class Religioncard(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    question=db.Column(db.String(1000))
    answer=db.Column(db.String(100))

class Sciencecard(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    question=db.Column(db.String(1000))
    answer=db.Column(db.String(100))

class Socialsciencecard(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    question=db.Column(db.String(1000))
    answer=db.Column(db.String(100))

class Sportscard(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    question=db.Column(db.String(1000))
    answer=db.Column(db.String(100))

class Visualartcard(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    question=db.Column(db.String(1000))
    answer=db.Column(db.String(100))

""""

class Test(db.Model):
    user_topic_attempt=db.Column(db.Integer, primary_key=True)

class Test_Card(db.Model): 
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))  
    topic_id=db.Column(db.Integer, db.ForeignKey('topic.id')) 
    user_topic_attempt=db.Column(db.Integer, db.ForeignKey('test.user_topic_attempt'))  
    card_id=db.Column(db.Integer, db.ForeignKey('card.id'))
    attempt_date=db.Column(db.DateTime(timezone=True), default=func.now())
"""