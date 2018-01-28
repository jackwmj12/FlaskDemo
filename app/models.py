from flask_login import UserMixin
from .import login_manager
from . import db
from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.objects(role_id = user_id).first()

class User(UserMixin,db.Document):
    meta = {'collection': 'OderawayAccount'}
    username = db.StringField()
    password_hash = db.StringField()
    phonenum = db.StringField()
    email = db.StringField()
    role_id = db.StringField()

    @property
    def password(self):
        raise AttributeError("password is not readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password=password)


    def verify_password(self, password):
        return check_password_hash(self.password_hash,str(password))


    def __repr__(self):
        return '<User %r>' % self.username