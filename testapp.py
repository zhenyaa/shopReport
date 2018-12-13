import os
from app import app,db
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.testing = True
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    def test_load_js(self):
        rv = self.app.get('/')
        assert b'<app-root></app-root>' in rv.data

    def login(self, username, password):
        return self.app.post('/login', data=dict(name = username, "pass" = password), follow_redirects=True)

    def logout(self):
        return self.app.delete('/logout', follow_redirects=True)

    def test_login_logout(self):
        rv = self.login('central', '12358134')
        print(rv.data)
        assert b'You were logged in' in rv.data
        rv = self.logout()
        assert b'You were logged out' in rv.data
        # rv = self.login('adminx', 'default')
        # assert b'Invalid username' in rv.data
        # rv = self.login('admin', 'defaultx')
        # assert b'Invalid password' in rv.data

if __name__ == '__main__':
    unittest.main()