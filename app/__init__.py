from flask import Flask
from flask_apscheduler import APScheduler
from flask_sqlalchemy import SQLAlchemy
from config import Config


db = SQLAlchemy()
scheduler = APScheduler()


def create_app():
    """
    Initialize the core app.
    """
    app = Flask(__name__)
    # Initialize Config
    app.config.from_object(Config)
    # db initialization
    db.init_app(app)
    # scheduler initialization
    scheduler.init_app(app)
    scheduler.start()
    with app.app_context():
        from . import actions
        return app
