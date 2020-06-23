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
    quizzes = db.relationship('Quiz', backref='user', lazy=True)


    def __init__(self, public_id, email, password, nickname):
      self.public_id = public_id
      self.email = email
      self.password = password
      self.nickname = nickname


class Quiz(db.Model):
  __tablename__ = "quizzes"

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(50))
  info = db.Column(db.String(200))
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  questions = db.relationship('Question', backref='quiz', lazy=True)

  def __init__(self, title, info, user_id):
    self.title = title
    self.info = info
    self.user_id = user_id


class Question(db.Model):
   __tablename__ = "questions"

   id = db.Column(db.Integer, primary_key=True)
   question = db.Column(db.String(200), unique=True)
   ans_one = db.Column(db.String(200), nullable=False)
   ans_two = db.Column(db.String(200), nullable=False)
   ans_three = db.Column(db.String(200))
   ans_four = db.Column(db.String(200))
   correct = db.Column(db.Integer,nullable=False)
   quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'), nullable=False)
   
   
   

