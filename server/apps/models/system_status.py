from ext import db

class SystemStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_num = db.Column(db.Integer)
    blog_ptr = db.Column(db.Integer)