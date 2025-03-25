from app import db

class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    is_available = db.Column(db.Boolean(), nullable=False)
    type = db.Column(db.String(), nullable=False)

    def __init__(self, name, author_id, is_available, type):
        self.name = name
        self.author_id = author_id
        self.is_available = is_available
        self.type = type