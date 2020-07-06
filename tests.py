import unittest
from api import create_app
from api.config import *

class BasicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app_test = create_app(DevelopmentConf).test_client()
    
    def test_login(self):
        response = self.app_test.get('/api/login', headers={'Authorization': 'Basic bWFjaWVqOmxvbA=='})
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
        