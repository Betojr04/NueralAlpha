# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
jwt = JWTManager()


def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

    db.init_app(app)
    jwt.init_app(app)
    Migrate(app, db)

    # Import routes after app/db setup to avoid circular import
    from app.routes.home import home_bp
    from app.routes.api import api
    from app.routes.auth import auth

    app.register_blueprint(home_bp)
    app.register_blueprint(api)
    app.register_blueprint(auth, url_prefix="/")

    return app
