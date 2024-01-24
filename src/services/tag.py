import uuid

from pymysql import IntegrityError

from database import MysqlAccess, database
from helpers.constants import SQLQueries
from helpers.constants.http_statuses import HTTPStatuses
from helpers.exceptions import AlreadyExists


class TagService:
    def __init__(self, database_access=None):
        self.database_access = database_access or MysqlAccess(database)

    def get_tags(self):
        with self.database_access as dao:
            tags = dao.read(SQLQueries.GET_ALL_TAGS)
        return tags

    def create_tag(self, tag_name):
        try:
            with self.database_access as dao:
                dao.write(SQLQueries.CREATE_TAG, (uuid.uuid4(), tag_name))
        except IntegrityError:
            raise AlreadyExists(HTTPStatuses.CONFLICT.code, HTTPStatuses.CONFLICT.status, f"tag with name {tag_name} already exists!")

    def delete_tag(self):
        ...

    def update_tag(self):
        ...
