from helpers.constants import Strings
from helpers.constants.http_statuses import HTTPStatuses
from helpers.enum.user_role import UserRole
from helpers.exceptions import CustomException
from helpers.log import logger
from services.tag import TagService
from utils.rbac import validate_token_details


@validate_token_details(UserRole.ADMIN.value)
class DeleteTagController:
    def __init__(self, tag_id, tag_service=None):
        self.tag_id = tag_id
        self.tag_service = tag_service or TagService()

    def __call__(self):
        try:
            self.tag_service.delete_tag(self.tag_id)
        except CustomException as custom_error:
            logger.info(custom_error)
            return custom_error.dump(), custom_error.code
        else:
            return {Strings.RESULT: Strings.REMOVED}, HTTPStatuses.CREATED.code