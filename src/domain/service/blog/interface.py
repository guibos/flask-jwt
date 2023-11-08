from abc import ABC, abstractmethod
from typing import Iterable

from domain.entities.account.account_share import AccountShare
from domain.entities.post.post import Post
from domain.entities.post.post_id import PostId
from domain.enums.permission import Permission
from domain.service.authorization.authorization import Authorization


class BlogServiceInterface(ABC):
    @abstractmethod
    def get_post(self, post_id: PostId) -> Post:
        pass

    @Authorization(permissions={Permission.ADMIN})
    def delete_post(self, *, requester: AccountShare, post_id: PostId):
        self._delete_post(requester=requester, post_id=post_id)

    @abstractmethod
    def _delete_post(self, *, requester: AccountShare, post_id: PostId):
        pass
