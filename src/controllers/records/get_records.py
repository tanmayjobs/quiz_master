from helpers.constants import Strings
from services.record import RecordService


class GetRecordsController:
    def __init__(self, args, records_service=None):
        self.args = args
        self.records_service = records_service or RecordService()

    def __call__(self):
        records = self.records_service.get_records(self.args)
        return {Strings.RECORDS: records}, 200
