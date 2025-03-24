from routes.authors import author_routes
from routes.books import book_routes

def register_routes(app):
    app.register_blueprint(author_routes)
    app.register_blueprint(book_routes)