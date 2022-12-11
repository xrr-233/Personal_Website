from datetime import datetime
import jwt
import os
import base64
from hashlib import sha256

from flask import Blueprint, request, url_for, jsonify
from werkzeug.utils import secure_filename

from apps.models import *
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
    if (user == None):
        res.update({
            'status': 'failure',
            'msg': 'user_not_exist',
        })
    elif (user.password != sha256(password.encode('utf-8')).hexdigest()):
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
        res.update({'token': token})

    return jsonify(res)


@api.route('/change_password', methods=['GET', 'POST'])
def change_password():
    email = request.json.get('email')
    old_password = request.json.get('old_password')
    new_password = request.json.get('new_password')

    users = UserAccount.query.filter_by(email=email)
    user = None
    for u in users:
        user = u

    res = {
        'status': 'success',
    }
    if (user == None):
        res.update({
            'status': 'failure',
            'msg': 'user_not_exist',
        })
    elif (user.password != sha256(old_password.encode('utf-8')).hexdigest()):
        res.update({
            'status': 'failure',
            'msg': 'wrong_password',
        })
    else:
        user.password = sha256(new_password.encode('utf-8')).hexdigest()
        db.session.commit()

    return jsonify(res)


@api.route('/ask_for_blog_titles', methods=['GET', 'POST'])
def ask_for_blog_titles():
    max_title_num = int(request.json.get('max_title_num'))

    blog_articles = BlogArticle.query.all()
    blog_articles_list = []
    for b in blog_articles:
        blog_articles_list.append(b)
    blog_articles_list.reverse()

    res = {
        'number': len(blog_articles_list),
        'error': None,
        'blogs': [],
    }
    for i in range(0, min(max_title_num, len(blog_articles_list))):
        try:
            with open(os.getcwd() + url_for('static', filename=f'blog/{blog_articles_list[i].blog_filename}.md'),
                      'r') as f:
                res['blogs'].append({
                    'blog_title': blog_articles_list[i].blog_title,
                    'create_time': blog_articles_list[i].create_time.strftime('%Y-%m-%d %H:%M:%S'),
                })
        except:
            res.update({'error': 'critical'})

    return jsonify(res)


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
            with open(os.getcwd() + url_for('static', filename=f'blog/{blog_articles_list[i].blog_filename}.md'),
                      'r') as f:
                content = f.read()
            res['blogs'].append({
                'blog_filename': blog_articles_list[i].blog_filename,
                'blog_title': blog_articles_list[i].blog_title,
                'create_time': blog_articles_list[i].create_time.strftime('%Y-%m-%d %H:%M:%S'),
                'content': content,
            })
        except:
            res.update({'error': 'critical'})

    return jsonify(res)


@api.route('/delete_blog', methods=['GET', 'POST'])
def delete_blog():
    blog_filename = request.json.get('blog_filename')

    blog_articles = BlogArticle.query.filter_by(blog_filename=blog_filename)
    blog_article = None
    for b in blog_articles:
        blog_article = b

    res = {
        'status': 'success',
    }
    if (blog_article == None):
        res.update({
            'status': 'failure'
        })
    else:
        db.session.delete(blog_article)
        db.session.commit()

    return jsonify(res)


@api.route('/upload_blog', methods=['GET', 'POST'])
def upload_blog():
    blog_title = request.form.get('blog_title')
    form_file = request.files['form_file']

    res = {
        'status': 'success',
    }

    system_status_ = SystemStatus.query.all()
    system_status = None
    for s in system_status_:
        system_status = s

    if (system_status.blog_num >= 100000):
        res.update({
            'status': 'failure',
            'msg': 'database_full',
        })
    else:
        base_path = os.path.dirname(__file__)
        upload_path = os.path.join(base_path, f'{os.getcwd()}/static/blog',
                                   secure_filename(f'{str(system_status.blog_ptr).zfill(5)}.md'))
        form_file.save(upload_path)

        blog_article = BlogArticle()
        blog_article.blog_filename = str(system_status.blog_ptr).zfill(5)
        blog_article.blog_title = blog_title
        blog_article.create_time = datetime.now()
        db.session.add(blog_article)

        system_status.blog_num += 1
        system_status.blog_ptr += 1
        flag = False
        blog_article_ = BlogArticle.query.filter_by(blog_filename=str(system_status.blog_ptr).zfill(5))
        for b in blog_article_:
            flag = True
        while (system_status.blog_ptr > 99999 or flag):
            system_status.blog_ptr += 1
            flag = False
            blog_article_ = BlogArticle.query.filter_by(blog_filename=str(system_status.blog_ptr).zfill(5))
            for b in blog_article_:
                flag = True

        db.session.commit()

    return jsonify(res)


@api.route('/ask_for_announcement_titles', methods=['GET', 'POST'])
def ask_for_announcement_titles():
    max_title_num = int(request.json.get('max_title_num'))

    announcements = Announcement.query.all()
    announcements_list = []
    for a in announcements:
        announcements_list.append(a)
    announcements_list.reverse()

    res = {
        'number': len(announcements_list),
        'error': None,
        'announcements': [],
    }
    for i in range(0, min(max_title_num, len(announcements_list))):
        try:
            res['announcements'].append({
                'announcement_title': announcements_list[i].announcement_title,
                'create_time': announcements_list[i].create_time.strftime('%Y-%m-%d %H:%M:%S'),
            })
        except:
            res.update({'error': 'critical'})

    return jsonify(res)


@api.route('/upload_announcement', methods=['GET', 'POST'])
def upload_announcement():
    announcement_title = request.form.get('announcement_title')
    form_content = request.form.get('form_content')

    res = {
        'status': 'success',
    }

    announcement = Announcement()
    announcement.announcement_title = announcement_title
    announcement.announcement_content = form_content
    announcement.create_time = datetime.now()
    db.session.add(announcement)
    db.session.commit()

    return jsonify(res)


@api.route('/get_collections', methods=['GET', 'POST'])
def get_collections():
    collections = Collection.query.all()
    collections_list = []
    for c in collections:
        collections_list.append(c)
    collections_list.reverse()

    res = {
        'number': len(collections_list),
        'error': None,
        'collections': [],
    }
    for i in range(0, len(collections_list)):
        try:
            res['collections'].append({
                'id': collections_list[i].id,
                'proj_title': collections_list[i].proj_title,
                'proj_link': collections_list[i].proj_link,
            })
        except:
            res.update({'error': 'critical'})

    return jsonify(res)


@api.route('/get_collection_img', methods=['GET', 'POST'])
def get_collection_img():
    id = int(request.json.get('id'))

    collections = Collection.query.filter_by(id=id)
    collection = None
    for c in collections:
        collection = c

    res = {
        'error': None,
        'base64': None,
    }
    if (collection != None):
        path = url_for('static', filename=f'imgs/collection/{collection.img_filename}.{collection.img_type}')
        with open(f"{os.getcwd()}/{path}", "rb") as f:  # 转为二进制格式
            base64_data = base64.b64encode(f.read())  # 使用base64进行加密
        res.update({'base64': str(base64_data, encoding="utf-8")})
    else:
        res.update({'error': 'critical'})

    return jsonify(res)
