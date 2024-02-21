"""
The blueprint package contains all the blueprints for the project and also contains the register_blueprints,
which is used to register the necessary blueprints of the application.
"""

from flask_smorest import Api

from helpers.constants import LogText
from .auth import blp as AuthBlp
from .options import blp as OptionBlp
from .questions import blp as QuestionsBlp
from .quizzes import blp as QuizzesBlp
from .records import blp as RecordsBlp
from .tags import blp as TagsBlp
from .users import blp as UsersBlp


def register_blueprints(app):
    """
    Takes flask app as an argument and register all the blueprints.
    :param app: Flask app
    :return: None
    """
    app.logger.info(LogText.REGISTERING_BLUEPRINTS)
    api = Api(app)
    api.register_blueprint(AuthBlp)
    api.register_blueprint(QuizzesBlp)
    api.register_blueprint(QuestionsBlp)
    api.register_blueprint(OptionBlp)
    api.register_blueprint(TagsBlp)
    api.register_blueprint(RecordsBlp)
    api.register_blueprint(UsersBlp)
    app.logger.info(LogText.REGISTERING_BLUEPRINTS_COMPLETED)


__all__ = ["register_blueprints"]
