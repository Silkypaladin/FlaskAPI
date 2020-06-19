from .extensions.database import db

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    nickname = db.Column(db.String(100), unique=True)
    active = db.Column(db.Boolean(), default=True)
    date_created = db.Column(db.DateTime, default=db.func.now())


    def def __init__(self, email, password, nickname, active, date_created):
      self.email = email
      self.password = password
      self.nickname = nickname
      self.active = active
      self.date_created = date_created
