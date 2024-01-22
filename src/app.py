from flask import Flask
from flask_smorest import Api
from dotenv import load_dotenv

from blueprints import AuthBlp, QuizzesBlp, UsersBlp, RecordsBlp, QuestionsBlp, OptionBlp

import os


def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.secret_key = os.getenv("APP_SECRET_KEY")
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
    api = Api(app)
    api.register_blueprint(AuthBlp)
    api.register_blueprint(QuizzesBlp)
    api.register_blueprint(QuestionsBlp)
    api.register_blueprint(OptionBlp)
    api.register_blueprint(RecordsBlp)
    api.register_blueprint(UsersBlp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
