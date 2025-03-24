from app import db

class Author(db.Model):
    __tablename__ = 'author'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=False)
    books = db.relationship('Book', backref='author', lazy=True)

    def __init__(self, name):
        self.name = name