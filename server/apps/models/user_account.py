from ext import db
from datetime import datetime

class UserAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(length=20), nullable=False)
    password = db.Column(db.String(length=64), nullable=False)
    nickname = db.Column(db.String(length=20))
    email = db.Column(db.String(length=60))
    create_time = db.Column(db.DateTime, default=datetime.now)
    authority = db.Column(db.Integer)