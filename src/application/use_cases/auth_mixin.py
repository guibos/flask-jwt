from flask import request

from domain.value_objects.authentication import Authentication


class AuthMixin:
    @staticmethod
    def _get_authentication() -> Authentication:
        username = request.authorization.username if request.authorization else None
        password = request.authorization.password if request.authorization else None
        token = request.authorization.token if request.authorization else None

        return Authentication(
            username=username,
            password=password,
            token=token
        )