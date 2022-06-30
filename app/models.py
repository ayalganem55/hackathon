from app import db

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    category = db.Column(db.String(64))
    phone = db.Column(db.Integer)
    email = db.Column(db.String(64))
    website = db.Column(db.String(64))
    facebook = db.Column(db.String(64))
    address = db.Column(db.String(64))
    sentence = db.Column(db.String(64))

