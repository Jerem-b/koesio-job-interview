from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_cors import CORS
from routes import register_routes

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    db.init_app(app)
    Migrate(app, db)

    register_routes(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0")