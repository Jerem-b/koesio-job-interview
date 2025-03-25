from routes.authors import author_routes
from routes.books import book_routes
from routes.users import user_routes
from routes.borrows import borrow_routes

def register_routes(app):
    app.register_blueprint(author_routes)
    app.register_blueprint(book_routes)
    app.register_blueprint(user_routes)
    app.register_blueprint(borrow_routes)