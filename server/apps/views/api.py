import json
import os
from hashlib import sha256

from flask import Blueprint, jsonify, request, url_for
from ext import db

from apps.models.blog_article import BlogArticle
from apps.models.user_account import UserAccount

api = Blueprint('index', __name__)

global_user = None


@api.route('/get_user_status', methods=['GET'])
def get_user_status():
    res = {
        'user': None
    }

    global global_user
    if(global_user != None):
        res = {
            'user': {
                'user_name': global_user.user_name,
                'nickname': global_user.nickname,
                'email': global_user.email,
                'create_time': global_user.create_time.strftime('%Y-%m-%d %H:%M:%S'),
                'authority': global_user.authority,
            }
        }

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
        global global_user
        global_user = user

    return json.dumps(res)

@api.route('/logout', methods=['GET', 'POST'])
def logout():
    email = request.json.get('email')

    res = {
        'status': 'failure',
    }

    global global_user
    if(email == global_user.email):
        global_user = None
        res.update({
            'status': 'success',
        })

    return json.dumps(res)
