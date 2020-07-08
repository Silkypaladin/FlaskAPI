import unittest
from api import create_app
from api.config import *
import json
from api.models import User

class RoutesTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app(TestConf)
        cls.app_test = cls.app.test_client()
        response = cls.app_test.get('/api/login', headers={'Authorization': 'Basic YWRtaW46YWRtaW4='})
        data = json.loads(response.get_data(as_text=True))
        cls.token = data['token']
    
    def test_add_user_correct(self):
        response = self.app_test.post('/api/user', json={'email' : 'email@test', 'password' : 'pass', 'nickname' : 'nick'}
        ,  headers={'x-access-token': self.token})
        self.assertEqual(response.status_code, 200)

    def test_add_user_error(self):
        response = self.app_test.post('/api/user', json={'email' : 'email@test', 'password' : 'pass', 'nickname' : 'nick'}
        ,  headers={'x-access-token': self.token})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['message'], 'User already exists!')

    def test_delete_user_correct(self):
        with self.app.app_context():
            user = User.query.filter_by(nickname='nick').first()
        public_id = user.public_id
        response = self.app_test.delete(f'/api/user/{public_id}',  headers={'x-access-token': self.token})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
    
    def test_delete_user_no_user(self):
        response = self.app_test.delete('/api/user/111',  headers={'x-access-token': self.token})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['message'], 'No user found.')
    
    def test_get_all_users(self):
        response = self.app_test.get('/api/user', headers={'x-access-token': self.token})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(data), 1)
    
    def test_get_one_user(self):
        with self.app.app_context():
            user = User.query.filter_by(nickname='admin').first()
        public_id = user.public_id
        response = self.app_test.get(f'/api/user/{public_id}', headers={'x-access-token': self.token})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['nickname'], 'admin')

    def test_quiz_add_quiz(self):
        response = self.app_test.post('/api/quizzes', json = {
            'title': 'Test quiz',
            'info': 'Test quiz info'
        }, headers={'x-access-token' : self.token})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['message'], 'New quiz added.')
    
    def test_quiz_add_title_exists(self):
        response = self.app_test.post('/api/quizzes', json = {
            'title': 'Test quiz',
            'info': 'Test quiz info'
        }, headers={'x-access-token' : self.token})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['message'], 'Could not add quiz.')
    
    def test_quiz_delete(self):
        response = self.app_test.delete('/api/quizzes/1', headers={'x-access-token' : self.token})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['message'], 'Quiz deleted.')



if __name__ == "__main__":
    unittest.main()
        