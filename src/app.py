from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

from blueprints import (
    AuthBlp,
    QuizzesBlp,
    UsersBlp,
    RecordsBlp,
    TagsBlp,
    QuestionsBlp,
    OptionBlp,
)
import os

from helpers.constants.http_statuses import HTTPStatuses
from helpers.exceptions import NotEnoughPermission, ValidationCustomException


def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.secret_key = os.getenv("APP_SECRET_KEY")
    app.config["PORT"] = 9000
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
    app.json.sort_keys = False

    app.register_error_handler(
        NotEnoughPermission, lambda err: (err.dump(), HTTPStatuses.FORBIDDEN.code)
    )
    app.register_error_handler(
        ValidationCustomException,
        lambda err: (err.dump(), HTTPStatuses.UNPROCCESSABLE_ENTITY.code),
    )

    jwt = JWTManager(app)

    @jwt.expired_token_loader
    def expired_token(jwt_header, jwt_payload):
        return {"error": "token expired"}, 401

    @jwt.invalid_token_loader
    def invalid_token(error):
        return {"error": "invalid token"}, 401

    @jwt.unauthorized_loader
    def unauthorized(error):
        return {"error": "token not provided"}, 401

    api = Api(app)
    api.register_blueprint(AuthBlp)
    api.register_blueprint(QuizzesBlp)
    api.register_blueprint(QuestionsBlp)
    api.register_blueprint(OptionBlp)
    api.register_blueprint(TagsBlp)
    api.register_blueprint(RecordsBlp)
    api.register_blueprint(UsersBlp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
