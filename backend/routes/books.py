from flask import Blueprint, request
from sqlalchemy import or_
from app import db
from models.books import Book
from models.authors import Author

book_routes = Blueprint('books', __name__)

@book_routes.route('/books', methods=['POST', 'GET'])
def handle_books():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()

            book = Book(
                name=data['name'],
                author_id=data['author_id'],
                is_available=data['is_available'],
                type=data['type'],
            )
            db.session.add(book)
            db.session.commit()
            return {"message": f"Book {book.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format."}

    elif request.method == 'GET':
        books = Book.query.all()
        results = [
        {
            'id': book.id,
            'name': book.name,
            'author_id': book.author_id,
            'author_name': book.author.name,
            'is_available': book.is_available,
            'type': book.type,
        } for book in books]

    return {"count": len(results), "books": results}


@book_routes.route('/books/<book_id>', methods=['GET', 'PATCH', 'DELETE'])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)

    if request.method == 'GET':
        response = {
            'id': book.id,
            'name': book.name,
            'author_id': book.author_id,
            'author_name': book.author.name,
            'is_available': book.is_available,
            'type': book.type,
        }
        return {"message": "Success", "book": response}

    elif request.method == 'PATCH':
        data = request.get_json()
        for key, value in data.items():
            setattr(book, key, value)
        db.session.commit()
        return {"message": f"Book {book.name} successfully updated."}

    elif request.method == 'DELETE':
        try:
            db.session.delete(book)
            db.session.commit()
            return {"message": f"Book {book.name} successfully deleted."}
        except:
            return {"message": "Error while deleting book."}
    
@book_routes.route('/books/available', methods=['GET'])
def get_available_books():
    books = Book.query.filter(Book.is_available == True).all()
    results = [
        {
            'id': book.id,
            'name': book.name,
            'author_id': book.author_id,
            'author_name': book.author.name,
            'is_available': book.is_available,
            'type': book.type,
        } for book in books]

    return {"count": len(results), "books": results}

@book_routes.route('/books/search', methods=['GET'])
def search_book():
    params = request.args.to_dict(flat=False)
    query = Book.query

    if 'name' in params:
        query = query.filter(or_(*[Book.name.ilike(f"%{name}%") for name in params['name']]))

    if 'author' in params:
        query = query.join(Author)
        query = query.filter(or_(*[Author.name.ilike(f"%{author}%") for author in params['author']]))

    if 'type' in params:
        query = query.filter(or_(*[Book.type.ilike(f"%{type}%") for type in params['type']]))

    books = query.all()
    results = [
        {
            'id': book.id,
            'name': book.name,
            'author_id': book.author_id,
            'author_name': book.author.name,
            'is_available': book.is_available,
            'type': book.type,
        } for book in books]

    return {"count": len(results), "books": results}