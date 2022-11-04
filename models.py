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


#part 3, creating a posttag model
class PostTag(db.Model):
    """joins together a post and a tag, have foreign key post_id and tag_id"""
    """want post and tag to be unique and not null"""
    __tablename__ = 'poststag'
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'),
    primary_key = True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'),
    primary_key = True)
    #Recall we can actually put 2 of these as primary keys in M2M

#now we need a TAG model
class Tag(db.Model):
    """Tags for posts"""
    __tablename__ = 'tags'
    tag_id = db.Column(db.Integer, primary_key = True)
    tag_name = db.Column(db.Integer, primary_key = True)

    posts = db.relationship('Post', secondary = 'poststag',
    backref = 'tags')


def connect_db(app):

    db.app = app 
    db.init_app(app)

