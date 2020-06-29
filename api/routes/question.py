from flask import Blueprint, jsonify, request
from ..extensions.database import db
from .login import token_required
from ..models import Quiz, Question

question = Blueprint('question', __name__)

@question.route('/api/question/<quiz_id>', methods=['GET'])
@token_required
def get_all_questions(current_user, quiz_id):
    questions = Question.query.filter_by(quiz_id=quiz_id).all()
    output = []
    for q in questions:
        q_data = {}
        q_data['id'] = q.id
        q_data['question'] = q.question
        q_data['ans_one'] = q.ans_one
        q_data['ans_two'] = q.ans_two
        q_data['ans_three'] = q.ans_three
        q_data['ans_four'] = q.ans_four
        q_data['correct'] = q.correct
        q_data['quiz_id'] = quiz_id
        output.append(q_data)
    return jsonify(output)

@question.route('/api/question/<quiz_id>', methods=['POST'])
@token_required
def add_question(current_user, quiz_id):
    data = request.get_json()
    new_question = Question(data['question'], data['ans_one'], data['ans_two'], data['ans_three'], data['ans_four'], data['correct'], quiz_id)
    try:
        db.session.add(new_question)
        db.session.commit()
    except:
        return jsonify({'message' : 'Could not add question.'})
    return jsonify({'message' : 'Question added.'})

@question.route('/api/question/<quiz_id>/<question_id>', methods=['DELETE'])
@token_required
def delete_question(current_user, quiz_id, question_id):
    question = Question.query.filter_by(id=question_id).first()
    if not question:
        return jsonify({'message' : 'No question found.'})
    db.session.delete(question)
    db.session.commit()
    return jsonify({'message' : 'Question deleted.'})