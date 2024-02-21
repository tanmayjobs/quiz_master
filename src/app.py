"""
This file is the entry point of the application.
Handles the creation of flask app and registering various other things for it such as,
    1. blueprints
    2. jwt
    3. configs
    4. error handlers
"""

from flask import Flask

from database import init_db
from blueprints import register_blueprints
from config import config_app
from helpers.exceptions import register_error_handlers
from helpers.jwt import register_jwt


# Implement logging properly
# Add Docstrings X
# Remove Caching Mechanism X
# Switch to only one type of database X


def create_app():
    """
    This function creates a flask app and registers various handlers for the app.
    :return: Flask app, an instance of Flask
    """
    app = Flask(__name__)

    config_app(app)
    register_error_handlers(app)
    register_blueprints(app)
    register_jwt(app)
    init_db(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
