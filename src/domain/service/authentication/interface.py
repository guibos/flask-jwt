from abc import ABC

from domain.entities.account.account_share import AccountShare
from domain.value_objects.authentication import Authentication


class AuthenticationServiceInterface(ABC):
    def get_authentication_token(self, authentication: Authentication) -> str:
        pass

    def get_data_from_token(self, authentication: Authentication) -> AccountShare:
        pass
