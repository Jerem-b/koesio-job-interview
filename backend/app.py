from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://root:root@db:5432/interview_db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=False)
    author = db.Column(db.String(), nullable=False)
    is_available = db.Column(db.Boolean(), nullable=False)
    type = db.Column(db.String(), nullable=False)

    def __init__(self, name, author, is_available, type):
        self.name = name
        self.author = author
        self.is_available = is_available
        self.type = type

    @app.route('/books', methods=['POST', 'GET'])
    def handle_books():
        if request.method == 'POST':
            if request.is_json:
                data = request.get_json()
                book = Book(
                    name=data['name'],
                    author=data['author'],
                    is_available=data['is_available'],
                    type=data['type'],
                )
                db.session.add(book)
                db.session.commit()
                return {"message": f"Book {book.name} has been created successfully."}
            else:
                return {"error": "The request payload is not in JSON format"}

        elif request.method == 'GET':
            books = Book.query.all()
            results = [
            {
                'name': book.name,
                'author': book.author,
                'is_available': book.is_available,
                'type': book.type,
            } for book in books]

        return {"Count": len(results), "Books": results}
    

    @app.route('/books/<book_id>', methods=['GET', 'PATCH', 'DELETE'])
    def update_book(book_id):
        book = Book.query.get_or_404(book_id)

        if request.method == 'GET':
            response = {
                'name': book.name,
                'author': book.author,
                'is_available': book.is_available,
                'type': book.type,
            }
            return {"message": "Success", "book": response}

        elif request.method == 'PATCH':
            data = request.get_json()
            for key, value in data.items():
                setattr(book, key, value)
            db.session.commit()
            return {"message": f"Book {book.name} successfully updated"}

        elif request.method == 'DELETE':
            db.session.delete(book)
            db.session.commit()
            return {"message": f"Book {book.name} successfully deleted."}
        
    @app.route('/books/available', methods=['GET'])
    def get_available_books():
        books = Book.query.filter(Book.is_available == True).all()
        results = [
            {
                'name': book.name,
                'author': book.author,
                'is_available': book.is_available,
                'type': book.type,
            } for book in books]

        return {"Count": len(results), "Books": results}

    @app.route('/books/search', methods=['GET'])
    def search_book():
        params = request.args.to_dict(flat=False)
        query = Book.query

        if 'name' in params:
            query = query.filter(or_(*[Book.name.ilike(f"%{name}%") for name in params['name']]))

        if 'author' in params:
            query = query.filter(or_(*[Book.author.ilike(f"%{author}%") for author in params['author']]))
        
        if 'type' in params:
            query = query.filter(or_(*[Book.type.ilike(f"%{type}%") for type in params['type']]))

        books = query.all()
        results = [
            {
                'name': book.name,
                'author': book.author,
                'is_available': book.is_available,
                'type': book.type,
            } for book in books]

        return {"Count": len(results), "Books": results}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')