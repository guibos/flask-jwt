import json

import jwt

from domain.entities.account.account import Account
from domain.entities.account.account_share import AccountShare
from domain.enums.permission import Permission
from domain.service.authentication.exceptions.invalid_authentication_error import InvalidAuthenticationError
from domain.service.authorization.exceptions.unauthorized_error import UnauthorizedError
from domain.value_objects.authentication import Authentication


class AuthenticationService:
    _JWT_SECRET = "secret"  # TODO: config file
    _JWT_ALGORITHM = "HS256"  # TODO: config file

    def __init__(self):
        self._accounts = {
            "admin": Account(account_id=1, username='admin', password="admin", permissions=[Permission.ADMIN]),
            "user": Account(account_id=2, username='user', password="pass", permissions=[Permission.READ]),
        }

    def get_authentication_token(self, authentication: Authentication) -> str:
        account = self._authenticate(authentication)

        account_payload = AccountShare(
            account_id=account.account_id, permissions=account.permissions, username=account.username)
        # Fixme: Bad workaround
        data = json.loads(account_payload.model_dump_json())
        return jwt.encode(data, self._JWT_SECRET, algorithm=self._JWT_ALGORITHM)

    def get_data_from_token(self, authentication: Authentication) -> AccountShare:
        if not authentication.token:
            raise UnauthorizedError

        data = jwt.decode(authentication.token, self._JWT_SECRET, algorithms=self._JWT_ALGORITHM)
        return AccountShare(**data)

    def _authenticate(self, authentication: Authentication) -> AccountShare:
        try:
            account = self._accounts[authentication.username]
        except KeyError:
            raise InvalidAuthenticationError
        if authentication.password != account.password:
            raise InvalidAuthenticationError
        return account
