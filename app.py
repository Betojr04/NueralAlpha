from flask import Flask
from routes.home import home_bp
from routes.api import api


def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(api)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
