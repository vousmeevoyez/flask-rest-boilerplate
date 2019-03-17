"""
    Flask App
    ______________________
    Package Initialization
"""
import os
from flask  import Flask

from mongoengine import connect

from flask_marshmallow  import Marshmallow

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

from app.config import config

ma = Marshmallow()
sentry = sentry_sdk

def db_connection(app):
    """ initialize connection to mongo db"""
    connect(
        db=app.config['DATABASE']['NAME'],
        host=app.config['MONGO_URI']
    )

def register_extension(app):
    """
        register flask extension via application factory
    """
    # marshmallow
    ma.init_app(app)

    # setup sentry only for production build
    if not app.testing and not app.debug:
        sentry_sdk.init(
            integrations=[FlaskIntegration()]
        )

def create_app(config_name):
    """
        Create flask instance
        args :
            config_name -- Configuration key used (DEV/PROD/TESTING)
    """
    app = Flask(__name__)
    app.config.from_object(config.CONFIG_BY_NAME[config_name])

    db_connection(app)
    register_extension(app)
    return app
