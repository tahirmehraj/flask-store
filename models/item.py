from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Coloum(db.Integer, primary_key=True)
    name = db.Coloum(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False)

