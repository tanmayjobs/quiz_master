import uuid

from pymysql import IntegrityError

from database import MysqlAccess
from helpers.constants import SQLQueries, Errors
from helpers.exceptions import AlreadyExists, DoNotExists


class TagService:
    def __init__(self, database_access=None):
        self.database_access = database_access or MysqlAccess()

    def get_tags(self):
        with self.database_access as dao:
            tags = dao.read(SQLQueries.GET_ALL_TAGS)
        return tags

    def create_tag(self, tag_name):
        try:
            tag_id = uuid.uuid4()
            with self.database_access as dao:
                dao.write(SQLQueries.CREATE_TAG, (tag_id, tag_name))
        except IntegrityError:
            raise AlreadyExists(Errors.TAG_ALREADY_EXISTS.format(tag_name))
        else:
            return tag_id

    def delete_tag(self, tag_id):
        with self.database_access as dao:
            tag = dao.read(SQLQueries.GET_TAG, (tag_id,))
            if not tag:
                raise DoNotExists(Errors.TAG_NOT_FOUND.format(id=tag_id))
            dao.write(SQLQueries.REMOVE_TAG, (tag_id,))

    def update_tag(self, tag_id, tag_name):
        with self.database_access as dao:
            tag = dao.read(SQLQueries.GET_TAG, (tag_id,))
            if not tag:
                raise DoNotExists(Errors.TAG_NOT_FOUND.format(id=tag_id))
            dao.write(
                SQLQueries.UPDATE_TAG,
                (
                    tag_name,
                    tag_id,
                ),
            )