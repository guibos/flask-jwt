from typing import List, Set

from domain.entities.account.account_share import AccountShare
from domain.enums.permission import Permission
from domain.service.authorization.exceptions.unauthorized_error import UnauthorizedError


class Authorization:
    def __init__(self, permissions: Set[Permission]):
        self._permissions = permissions

    def __call__(self, function):
        def wrapper(*args, requester: AccountShare, **kwargs):
            if self._permissions - set(requester.permissions):
                raise UnauthorizedError
            value = function(*args, requester=requester, **kwargs)
            return value

        return wrapper
