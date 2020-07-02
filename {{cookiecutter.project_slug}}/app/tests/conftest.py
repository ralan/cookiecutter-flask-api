import os

import sys
import pytest

from flask_migrate import upgrade as upgrade_db, downgrade as downgrade_db

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from {{cookiecutter.project_slug}}.factory import create_app  # noqa: E402


@pytest.fixture(scope='session')
def flask_app():
    app = create_app()

    app.config['DEBUG'] = True
    app.config['TESTING'] = True

    with app.app_context():
        yield app
        downgrade_db(revision='base')


@pytest.fixture(scope='session')
def client(flask_app):
    with flask_app.test_client() as client:
        yield client


@pytest.fixture(scope='function')
def init_db(flask_app):
    with flask_app.app_context():
        downgrade_db(revision='base')
        upgrade_db(revision='head')
        yield
