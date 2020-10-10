from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_blog import db , login_manager , app
from datetime import datetime
from flask_login import UserMixin

# We are going to create a load_user fun with user_id as an arg
# Add a decorator login_manager.user_loader

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# The class User is inheriting from the db model
class User(db.Model , UserMixin):
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(20) , nullable = False , unique = True)
    email = db.Column(db.String(120) , nullable = False , unique = True)
    image_file = db.Column(db.String(20) , nullable = False , default = 'default.jpg')
    password = db.Column(db.String(60) , nullable = False)
    posts = db.relationship('Post' , backref = 'author' , lazy = True)

    # A post can have only one user but a user can have multiple posts
    # lazy arg just defines when sqlalchemy loads the data fro the db
    # backref is similar to adding another Column to the post model
    # Upper case Post in user is because we are referencing the post class
    # Lower case user is because we are referencing the table and Column name

    def get_reset_token(self , expires_sec = 1800):
        s = Serializer(app.config['SECRET_KEY'] , expires_sec)
        return s.dumps({'user_id':self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}' , '{self.email}' , '{self.image_file}')"

class Post(db.Model ):
    id = db.Column(db.Integer , primary_key = True)
    title = db.Column(db.String(100) , nullable = False)
    date_posted = db.Column(db.DateTime , nullable = False , default = datetime.utcnow)
    content = db.Column(db.Text , nullable = False)
    user_id = db.Column(db.Integer , db.ForeignKey('user.id') , nullable = False)

    def __repr__(self):
        return f"Post('{self.title}' , '{self.date_posted}')" 
