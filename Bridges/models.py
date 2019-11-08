from Bridges import db,
from flask_login import UserMixin
from datetime import datetime

@Login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #username = db.Column(db.String(15), index=True ,unique=True)
    email = db.Column(db.String(50), index=True ,unique=True)
    password = db.Column(db.String(80))