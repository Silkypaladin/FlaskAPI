from .extensions.database import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    nickname = db.Column(db.String(100), unique=True)
    is_admin = db.Column(db.Boolean(), default=False)
    date_created = db.Column(db.DateTime, default=db.func.now())


    def __init__(self, public_id, email, password, nickname):
      self.public_id = public_id
      self.email = email
      self.password = password
      self.nickname = nickname
