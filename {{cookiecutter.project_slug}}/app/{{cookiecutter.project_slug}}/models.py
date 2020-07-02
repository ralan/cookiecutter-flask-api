from .db import db


class Item(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    sub_items = db.relationship('SubItem', backref='item', lazy=True)


class SubItem(db.Model):
    __tablename__ = 'sub_item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
