from flask import Blueprint, request
from app import db
from models.authors import Author


author_routes = Blueprint('authors', __name__)

@author_routes.route('/authors', methods=['POST', 'GET'])
def handle_authors():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            author = Author(
                name=data['name'],
            )
            db.session.add(author)
            db.session.commit()
            return {"message": f"Author {author.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        authors = Author.query.all()
        results = [
        {
            'id': author.id,
            'name': author.name,
            'book_ids': [book.id for book in author.books],
        } for author in authors]

    return {"count": len(results), "authors": results}

@author_routes.route('/authors/<author_id>', methods=['GET', 'PATCH', 'DELETE'])
def update_author(author_id):
    author = Author.query.get_or_404(author_id)

    if request.method == 'GET':
        response = {
            'id': author.id,
            'name': author.name,
            'books': [book.id for book in author.books],
        }
        return {"message": "Success", "author": response}

    elif request.method == 'PATCH':
        data = request.get_json()
        for key, value in data.items():
            setattr(author, key, value)
        db.session.commit()
        return {"message": f"Author {author.name} successfully updated"}

    elif request.method == 'DELETE':
        db.session.delete(author)
        db.session.commit()
        return {"message": f"Author {author.name} successfully deleted."}
    
@author_routes.route('/authors/<author_id>/books', methods=['GET'])
def search_book_by_author(author_id):
    author = Author.query.get_or_404(author_id)

    results = [
        {
            'id': author.id,
            'name': author.name,
            'books': [book.id for book in author.books],
        }
    ]

    return {'message': 'Success', 'books': results}