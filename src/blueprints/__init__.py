"""
The blueprint package contains all the blueprints for the project and also contains the register_blueprints,
which is used to register the necessary blueprints of the application.
"""

from flask_smorest import Api

from helpers.constants import LogText
from helpers.log import logger
from .auth import blp as AuthBlp
from .quizzes import blp as QuizzesBlp
from .users import blp as UsersBlp
from .records import blp as RecordsBlp
from .questions import blp as QuestionsBlp
from .options import blp as OptionBlp
from .tags import blp as TagsBlp


def register_blueprints(app):
    """
    Takes flask app as an argument and register all the blueprints.
    :param app: Flask app
    :return: None
    """
    logger.info(LogText.REGISTERING_BLUEPRINTS)
    api = Api(app)
    api.register_blueprint(AuthBlp)
    api.register_blueprint(QuizzesBlp)
    api.register_blueprint(QuestionsBlp)
    api.register_blueprint(OptionBlp)
    api.register_blueprint(TagsBlp)
    api.register_blueprint(RecordsBlp)
    api.register_blueprint(UsersBlp)
    logger.info(LogText.REGISTERING_BLUEPRINTS_COMPLETED)


__all__ = ["register_blueprints"]
