from app import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    borrows = db.relationship('Borrow', backref='user', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password
