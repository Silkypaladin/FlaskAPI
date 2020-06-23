from flask import Blueprint, jsonify, request
from ..extensions.database import db
from .login import token_required
from ..models import Quiz, Question

quiz = Blueprint('quiz', __name__)


@quiz.route('/api/quizzes', methods=['GET'])
@token_required
def get_all_quizzes(current_user):
    quizzes = Quiz.query.filter_by(user_id=current_user.public_id).all()
    output = []
    for quiz in quizzes:
        n_of_questions = Question.query.filter_by(quiz_id=quiz.id).count()
        quiz_data = {}
        quiz_data['id'] = quiz.id
        quiz_data['title'] = quiz.title
        quiz_data['info'] = quiz.info
        quiz_data['user_id'] = quiz.user_id
        quiz_data['number_of_questions'] = n_of_questions
        output.append(quiz_data)
    return jsonify(output)

@quiz.route('/api/quizzes', methods=['POST'])
@token_required
def create_new_quiz(current_user):
    data = request.get_json()
    title_exists = Quiz.query.filter((Quiz.user_id == current_user.public_id) & 
    (Quiz.title == data['title'])).count()
    if not title_exists:
        new_quiz = Quiz(data['title'], data['info'], current_user.public_id)
        db.session.add(new_quiz)
        db.session.commit()
        return jsonify({'message': 'New quiz added.'})
    return jsonify({'message' : 'Quiz already exists!'})

@quiz.route('/api/quizzes/<quiz_id>', methods=['GET'])
@token_required
def get_one_quiz(current_user, quiz_id):
    quiz = Quiz.query.filter_by(id=quiz_id).first()
    n_of_questions = Question.query.filter_by(quiz_id=quiz.id).count()
    quiz_data = {}
    quiz_data['id'] = quiz.id
    quiz_data['title'] = quiz.title
    quiz_data['info'] = quiz.info
    quiz_data['user_id'] = quiz.user_id
    quiz_data['number_of_questions'] = n_of_questions
    return jsonify(quiz_data)
