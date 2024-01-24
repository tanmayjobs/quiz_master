from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

from blueprints import AuthBlp, QuizzesBlp, UsersBlp, RecordsBlp, QuestionsBlp, OptionBlp, TagsBlp

import os

from helpers.exceptions import NotEnoughPermission
from schemas import ValidationCustomException


def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.secret_key = os.getenv("APP_SECRET_KEY")
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Quizzes"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.2"
    app.config["OPENAPI_JSON_PATH"] = "api-spec.json"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_REDOC_PATH"] = "/redoc"
    app.config["OPENAPI_REDOC_URL"] = (
        "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"
    )
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["OPENAPI_RAPIDOC_PATH"] = "/rapidoc"
    app.config["OPENAPI_RAPIDOC_URL"] = "https://unpkg.com/rapidoc/dist/rapidoc-min.js"

    app.register_error_handler(NotEnoughPermission, lambda err: (err.dump(), err.code))
    app.register_error_handler(ValidationCustomException, lambda err: ({"error": str(err)}, 422))

    jwt = JWTManager(app)

    @jwt.expired_token_loader
    def expired_token(jwt_header, jwt_payload):
        return {
            "error": "token expired"
        }, 401

    @jwt.invalid_token_loader
    def invalid_token(error):
        return {
            "error": "invalid token"
        }, 401

    @jwt.unauthorized_loader
    def unauthorized(error):
        return {
            "error": "token not provided"
        }, 401

    api = Api(app)
    api.register_blueprint(AuthBlp)
    api.register_blueprint(QuizzesBlp)
    api.register_blueprint(QuestionsBlp)
    api.register_blueprint(OptionBlp)
    api.register_blueprint(RecordsBlp)
    api.register_blueprint(UsersBlp)
    api.register_blueprint(TagsBlp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
