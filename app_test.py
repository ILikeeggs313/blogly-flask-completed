from unittest import TestCase
from app import app
from models import DEFAULT_URL, db, User

#we use a separate test database so we dont clutter with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///sql_test'
app.config['SQLALCHEMY_ECHO'] = False

#make flask errors be real errors, rather than HTML pages with errors info
app.config['TESTING'] = True

#disable flask_Debugtoolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_app()
db.create_all()

class UserViewTestCase(TestCase):
    """Test for views for users"""
    def setUp(self):
        """Add sample user"""
        User.query.delete()

        user = user(first_name = 'TestUser', last_name = 'User',
        image_url = DEFAULT_URL)
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        """Clean up fouled transaction with rollback"""
        db.session.rollback()

    def test_list_users(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text= True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('TestUser', html)
    
    def test_show_users(self):
        with app.test_client() as client:
            resp = client.get('/users/new')
            html = resp.get_data(as_text= True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>User</h1>', html)
    def test_add_user(self):
        with app.test_client() as client:
            d = {'first_name': 'TestUser2',
            'last_name': 'User2', 'image_url': 'DEFAULT_URL'}
            resp = client.post('/', data = d, follow_redirects = True)
            html = resp.get_data(as_text= True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1> TestUser2</h1>', html)
    

    