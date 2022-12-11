from ext import db
from datetime import datetime

class Announcement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    announcement_title = db.Column(db.String(length=60))  # 上传到服务器的公告标题
    announcement_content = db.Column(db.String(length=1000))  # 上传到服务器的公告内容
    create_time = db.Column(db.DateTime, default=datetime.now)

class BlogArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_filename = db.Column(db.String(length=20))  # 上传到服务器的文章文件名
    blog_title = db.Column(db.String(length=60))  # 上传到服务器的文章标题
    create_time = db.Column(db.DateTime, default=datetime.now)
    # satisfactory # 作者对这篇文章的满意度
    # like = db.Column(db.Integer) # 点赞 待开发

class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img_filename = db.Column(db.String(length=20))  # 上传到服务器的图片文件名
    img_type = db.Column(db.String(length=10))  # 上传到服务器的图片格式
    proj_title = db.Column(db.String(length=60))  # 上传到服务器的项目标题
    proj_link = db.Column(db.String(length=1000))  # 项目链接


class SystemStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_num = db.Column(db.Integer)
    blog_ptr = db.Column(db.Integer)

class UserAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(length=20), nullable=False)
    password = db.Column(db.String(length=64), nullable=False)
    nickname = db.Column(db.String(length=20))
    email = db.Column(db.String(length=60))
    create_time = db.Column(db.DateTime, default=datetime.now)
    authority = db.Column(db.Integer)