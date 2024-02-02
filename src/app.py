"""
This file is the entry point of the application.
Handles the creation of flask app and registering various other things for it including,
    1. blueprints
    2. jwt
    3. configs
    4. error handlers
"""

from flask import Flask

from blueprints import register_blueprints
from config import config_app
from helpers.exceptions import register_error_handlers
from helpers.jwt import register_jwt


# Implement logging properly
# Add Docstrings
# Remove Caching Mechanism
# Switch to only one type of database


def create_app():
    app = Flask(__name__)

    config_app(app)
    register_error_handlers(app)
    register_blueprints(app)
    register_jwt(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
