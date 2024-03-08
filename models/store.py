from db import db


class StoreModel(db.Model):
    __tablename__ = "stores"
    id = db.Coloum(db.Interger, primary_key=True)
    name = db.Coloum(db.String(80, unique=True, nullable=False))
