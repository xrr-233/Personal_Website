import json
import os
import jwt
from hashlib import sha256

from flask import Blueprint, jsonify, request, url_for
from ext import db

from apps.models.blog_article import BlogArticle
from apps.models.user_account import UserAccount
from config import SECRET

api = Blueprint('index', __name__)

@api.route('/login', methods=['GET', 'POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    users = UserAccount.query.filter_by(email=email)
    user = None
    for u in users:
        user = u

    res = {
        'status': 'success',
    }
    if(user == None):
        res.update({
            'status': 'failure',
            'msg': 'user_not_exist',
        })
    elif(user.password != sha256(password.encode('utf-8')).hexdigest()):
        res.update({
            'status': 'failure',
            'msg': 'wrong_password',
        })
    else:
        payload = {
            'user_name': user.user_name,
            'nickname': user.nickname,
            'email': user.email,
            'create_time': user.create_time.strftime('%Y-%m-%d %H:%M:%S'),
            'authority': user.authority,
        }
        token = jwt.encode(payload, SECRET, algorithm='HS256')
        res.update({
            'token': token
        })

    return json.dumps(res)

@api.route('/ask_for_blogs', methods=['GET', 'POST'])
def ask_for_blogs():
    start_page = int(request.json.get('start_page'))
    per_page = int(request.json.get('per_page'))

    blog_articles = BlogArticle.query.all()
    blog_articles_list = []
    for b in blog_articles:
        blog_articles_list.append(b)
    blog_articles_list.reverse()

    res = {
        'number': min(per_page, len(blog_articles_list)),
        'error': None,
        'blogs': [],
    }
    for i in range((start_page - 1) * per_page, min(start_page * per_page - 1, len(blog_articles_list))):
        try:
            with open(os.getcwd() + url_for('static', filename=f'blog/{blog_articles_list[i].blog_filename}.md'), 'r') as f:
                content = f.read()
            res['blogs'].append({
                'blog_title': blog_articles_list[i].blog_title,
                'create_time': blog_articles_list[i].create_time.strftime('%Y-%m-%d %H:%M:%S'),
                'content': content,
            })
        except:
            res.update({'error': 'critical'})

    return json.dumps(res)
