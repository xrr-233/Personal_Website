from ext import db
from datetime import datetime

class BlogArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_filename = db.Column(db.String(length=20)) # 上传到服务器的文章文件名
    blog_title = db.Column(db.String(length=60))  # 上传到服务器的文章标题
    create_time = db.Column(db.DateTime, default=datetime.now)
    # satisfactory # 作者对这篇文章的满意度
    # like = db.Column(db.Integer) # 点赞 待开发