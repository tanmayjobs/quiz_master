from helpers.constants import Strings
from helpers.constants.http_statuses import HTTPStatuses
from helpers.exceptions import CustomException
from helpers.log import request_logger
from services.tag import TagService


class GetTagsController:
    def __init__(self, tag_service=None):
        self.tag_service = tag_service or TagService()

    def __call__(self):
        try:
            tags = self.tag_service.get_tags()
        except CustomException as custom_error:
            request_logger.info(custom_error)
            return custom_error.dump(), custom_error.code
        else:
            return {Strings.TAGS: tags}, HTTPStatuses.OK.code
