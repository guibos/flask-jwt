from typing import Iterable

from domain.entities.account.account_share import AccountShare
from domain.entities.post.post import Post
from domain.entities.post.post_id import PostId
from domain.enums.permission import Permission
from domain.service.authorization.authorization import Authorization
from domain.service.blog.exceptions.post_not_found_error import PostNotFoundError
from domain.service.blog.interface import BlogServiceInterface


class BlogService(BlogServiceInterface):

    def __init__(self):
        self._posts = {1: Post(
            post_id=1,
            title="Title 1",
            description="Description 1"
        )}

    def get_post(self, post_id: PostId) -> Post:
        try:
            return self._posts[post_id.post_id]
        except KeyError as e:
            raise PostNotFoundError from e

    def _delete_post(self, *, requester: AccountShare, post_id: PostId):
        pass
