from database.db import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(80), nullable=False)

    def __init__(self, firstname, lastname, email, message):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.message = message

    def __repr__(self) -> str:
        return f"Contact('{self.id}, {self.firstname}, {self.lastname}, {self.email}, {self.message}')"
