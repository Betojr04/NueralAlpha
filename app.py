from flask import Flask
from routes.home import home_bp
from routes.api import api
from routes.auth import auth_bp
import os
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)
    # load_dotenv()
    # app.secret_key = os.getenv("SECRET_KEY")
    app.secret_key = "secret"

    app.register_blueprint(home_bp)
    app.register_blueprint(api)
    app.register_blueprint(auth_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
