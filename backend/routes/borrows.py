from flask import Blueprint, request
from app import db
from models.borrows import Borrow
from models.books import Book
from models.users import User
from sqlalchemy import or_

borrow_routes = Blueprint('borrow', __name__)

@borrow_routes.route('/borrows/new', methods=['POST'])
def create_borrow():
    if request.is_json:
        try:
            data = request.get_json()
            book = Book.query.get(data['book_id'])
            if book.is_available == False:
                return {"message": "Error: Cannot borrow a book unavailable."}
            borrow = Borrow(
                user_id=data['user_id'],
                book_id=data['book_id'],
            )
            db.session.add(borrow)

            book.is_available = False

            db.session.commit()
            return {"message": f"Borrow {borrow.id} has been created successfully."}
        except:
            return {"message": "Error while creating new borrow."}
    else:
        return {"error": "The request payload is not in JSON format."}

@borrow_routes.route('/borrows/return/<borrow_id>', methods=['DELETE'])
def return_borrow(borrow_id):
    try:
        borrow = Borrow.query.get_or_404(borrow_id)
        book = Book.query.get(borrow.book_id)

        db.session.delete(borrow)
        book.is_available = True
        db.session.commit()
        return {"message": f"Borrow {borrow.id} successfully deleted."}
    except:
        return {"message": "Error while returning borrow."}

@borrow_routes.route('/borrows', methods=['GET'])
def current_borrows():
    borrows = Borrow.query.all()
    results = [
        {
            'id': borrow.id,
            'book_id': borrow.book_id,
            'user_id': borrow.user_id,
        } for borrow in borrows]

    return {"count": len(results), "borrows": results}

@borrow_routes.route('/borrows/search', methods=['GET'])
def search_borrows():
    params = request.args.to_dict(flat=False)
    query = Borrow.query

    if 'book' in params:
        query = query.join(Book)
        query = query.filter(or_(*[Book.name.ilike(f"%{name}%") for name in params['book']]))

    if 'user' in params:
        query = query.join(User)
        query = query.filter(or_(*[User.username == user for user in params['user']]))

    borrows = query.all()
    results = [
        {
            'id': borrow.id,
            'user_id': borrow.user_id,
            'book_id': borrow.book_id,
        } for borrow in borrows]

    return {"count": len(results), "borrows": results}