from helpers.constants.http_statuses import HTTPStatuses
from helpers.enum.user_role import UserRole
from helpers.exceptions import CustomException
from services.tag import TagService
from utils.rbac import accessed_by


@accessed_by(UserRole.ADMIN.value)
class CreateTagController:
    def __init__(self, json_data, tag_service=None):
        self.tag_name = json_data["tag_name"]
        self.tag_service = tag_service or TagService()

    def __call__(self):
        try:
            self.tag_service.create_tag(self.tag_name)
        except CustomException as custom_error:
            return custom_error.dump(), custom_error.code
        else:
            return {"created": "ok"}, HTTPStatuses.CREATED.code
