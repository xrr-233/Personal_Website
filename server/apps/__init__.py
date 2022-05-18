from flask import Flask
from flask_cors import CORS
import config
import ext
from apps.views.api import api
from apps.models.user_account import UserAccount
from apps.models.blog_article import BlogArticle
from apps.models.system_status import SystemStatus

def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config.from_object(config.DeveplomentConfig)
    app.register_blueprint(api)

    CORS(app, resources={r'/*': {'origins': '*'}})

    with app.app_context():
        ext.db.init_app(app)

    return app, ext.db
