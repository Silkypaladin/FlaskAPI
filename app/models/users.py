from ..extensions.database import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    nickname = db.Column(db.String(100), unique=True)
    active = db.Column(db.Boolean(), default=True)
    date_created = db.Column(db.DateTime, default=db.func.now())


    def __init__(self, public_id, email, password, nickname):
      self.public_id = public_id
      self.email = email
      self.password = password
      self.nickname = nickname

class Admin(db.Model):
  __tablename__="admins"

  id = db.Column(db.Integer, primary_key=True)
  public_id = db.Column(db.String(50), unique=True) 
  password = db.Column(db.String(100))
  nickname = db.Column(db.String(100), unique=True)

  def __init__(self, public_id, password, nickname):
    self.public_id = public_id
    self.password = password
    self.nickname = nickname