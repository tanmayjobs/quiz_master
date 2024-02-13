"""
This file contains config_app method which takes the flask app and set its configurations based on the .env file.
"""
import uuid

from dotenv import load_dotenv
import os

from flask import request

from helpers.constants import LogText


def config_app(app):
    app.logger.info(LogText.SETTING_UP_CONFIGS)
    load_dotenv()

    app.secret_key = os.getenv("APP_SECRET_KEY")
    app.json.sort_keys = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = os.getenv("API_TITLE")
    app.config["API_VERSION"] = os.getenv("API_VERSION")
    app.config["OPENAPI_VERSION"] = os.getenv("OPENAPI_VERSION")
    app.config["OPENAPI_JSON_PATH"] = os.getenv("OPENAPI_JSON_PATH")
    app.config["OPENAPI_URL_PREFIX"] = os.getenv("OPENAPI_URL_PREFIX")
    app.config["OPENAPI_REDOC_PATH"] = os.getenv("OPENAPI_REDOC_PATH")
    app.config["OPENAPI_REDOC_URL"] = os.getenv("OPENAPI_REDOC_URL")
    app.config["OPENAPI_SWAGGER_UI_PATH"] = os.getenv("OPENAPI_SWAGGER_UI_PATH")
    app.config["OPENAPI_SWAGGER_UI_URL"] = os.getenv("OPENAPI_SWAGGER_UI_URL")
    app.config["OPENAPI_RAPIDOC_PATH"] = os.getenv("OPENAPI_RAPIDOC_PATH")
    app.config["OPENAPI_RAPIDOC_URL"] = os.getenv("OPENAPI_RAPIDOC_URL")

    @app.before_request
    def attach_request_id():
        request.request_id = uuid.uuid4()

    app.logger.info(LogText.SETTING_UP_CONFIG_COMPLETED)
