from flask import Flask
from flask_cors import CORS
import config
import ext
from apps.api import api
from apps.models import *

def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config.from_object(config.DeveplomentConfig)
    app.register_blueprint(api)

    # CORS(app, resources={r'/*': {'origins': '*'}})
    CORS(app)

    with app.app_context():
        ext.db.init_app(app)

    return app, ext.db
