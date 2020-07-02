import pytest

from {{cookiecutter.project_slug}}.db import db
from {{cookiecutter.project_slug}}.models import Item


def test_01_migrations(init_db):
    assert db.engine.has_table('item')
    assert db.engine.has_table('sub_item')


def test_02_insert_item(init_db):
    item = Item(name='foo')
    db.session.add(item)
    db.session.commit()

    items = Item.query.all()

    assert len(items) == 1
    assert items[0].name == 'foo'
