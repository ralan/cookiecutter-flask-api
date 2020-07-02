import os
import connexion
from connexion.resolver import RestyResolver
from flask_migrate import Migrate

from .db import db


def create_app():
    app = connexion.FlaskApp(__name__, specification_dir='api')
    app.add_api('api.yaml', resolver=RestyResolver('{{cookiecutter.project_slug}}.api'))

    app = app.app

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if os.getenv('DB_URI'):
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
    else:
        db_host = os.getenv('DB_HOST', '{{cookiecutter.project_slug}}_db')
        db_name = os.getenv('DB_NAME', '{{cookiecutter.project_slug}}')
        db_user = os.getenv('DB_USER', 'root')
        db_password = os.getenv('DB_PASSWORD', '')
        app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{db_user}:{db_password}@{db_host}/{db_name}"

    db.init_app(app)
    Migrate(app, db)

    return app
