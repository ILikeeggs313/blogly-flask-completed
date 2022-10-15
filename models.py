"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()

DEFAULT_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"


#models go below:
class User(db.Model):
    """User model including id[PK], first_name, last_name,
    image_url"""
    __tablename__ = 'users'
    id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement = True)
    first_name = db.Column(db.String(50),
                    nullable = False,
                    unique = True)
    last_name = db.Column(db.String(50),
                    nullable = False,
                    unique = True)
    image_url = db.Column(db.string(100),
                    nullable = False,
                    default = DEFAULT_URL)
    
    @classmethod
    def full_name(self):
        """Return user's full name"""
        return f'{self.first_name} {self.last_name}'


    
    #primary key means unique and not null in SQL for id

#part 2
class Post(db.Model):
    """Blog post."""
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key = True)

    title = db.Column(db.Text, db.String(200), nullable = False)

    content = db.Column(db.Text, nullable = False)

    created_at = db.Column(db.DateTime, nullable = False,
    default = datetime.datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
    nullable = False)

def connect_db(app):

    db.app = app 
    db.init_app(app)
