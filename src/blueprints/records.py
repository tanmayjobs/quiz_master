from flask.views import MethodView
from flask_smorest import Blueprint

from controllers.records.get_records import GetRecordsController
from schemas import RecordFilter, Records

blp = Blueprint("Records", __name__)


@blp.route("/records")
class RecordsView(MethodView):
    @blp.arguments(RecordFilter, location="query")
    @blp.alt_response(200, schema=Records)
    def get(self, args):
        """
        Get quiz records based on filters.
        """
        get_records = GetRecordsController(args)
        return get_records()
