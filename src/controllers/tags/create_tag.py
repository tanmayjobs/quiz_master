from helpers.constants import Strings
from helpers.constants.http_statuses import HTTPStatuses
from helpers.enum.user_role import UserRole
from helpers.exceptions import CustomException
from helpers.log import request_logger
from services.tag import TagService
from utils.rbac import validate_token_details


@validate_token_details(UserRole.ADMIN.value)
class CreateTagController:
    def __init__(self, json_data, tag_service=None):
        self.tag_name = json_data[Strings.TAG_NAME]
        self.tag_service = tag_service or TagService()

    def __call__(self):
        try:
            tag_id = self.tag_service.create_tag(self.tag_name)
        except CustomException as custom_error:
            request_logger.info(custom_error)
            return custom_error.dump(), custom_error.code
        else:
            return {Strings.RESULT: Strings.CREATED, Strings.TAG_ID: tag_id}, HTTPStatuses.CREATED.code
