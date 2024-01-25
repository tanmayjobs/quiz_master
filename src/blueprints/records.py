from flask.views import MethodView
from flask_smorest import Blueprint


blp = Blueprint("Records", __name__)


@blp.route("/records")
class RecordsView(MethodView):
    def get(self):
        """
        Get quiz records based on filters.
        """
        ...
