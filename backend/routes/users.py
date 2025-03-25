from flask import Blueprint, request
from app import db
from models.users import User
from werkzeug.security import generate_password_hash, check_password_hash

user_routes = Blueprint('users', __name__)

@user_routes.route('/register', methods=['POST'])
def register():
    if request.is_json:
        data = request.get_json()
        user = User(
            username=data['username'],
            password=generate_password_hash(data['password']),
        )
        db.session.add(user)
        db.session.commit()
        return {"message": f"User {user.username} has been created successfully."}
    else:
        return {"error": "The request payload is not in JSON format"}

@user_routes.route('/login', methods=['POST'])
def login():
    if request.is_json:
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()

        if check_password_hash(user.password, data['password']):
            return {"message": f"User {user.username} sucessfully login."}
        else:
            return {"error": "Invalid username or password"}
    else:
        return {"error": "The request payload is not in JSON format"}
    
@user_routes.route('/users', methods=['GET'])
def list_users():
    users = User.query.all()
    results = [
    {
        'id': user.id,
        'username': user.username,
        'borrows': [
            {
                'id': borrow.id,
                'book_id': borrow.book_id,
                'user_id': borrow.user_id
            } for borrow in user.borrows
        ],
    } for user in users]

    return {"count": len(results), "users": results}