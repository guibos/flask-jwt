from flask import request, jsonify
from flask.views import MethodView

from application.use_cases.auth_mixin import AuthMixin
from domain.service.authentication.exceptions.invalid_authentication_error import InvalidAuthenticationError
from domain.service.authentication.interface import AuthenticationServiceInterface
from domain.value_objects.authentication import Authentication


class LoginView(MethodView, AuthMixin):
    def __init__(self, authentication_service: AuthenticationServiceInterface):
        self._authentication_service = authentication_service

    def get(self):
        auth = self._get_authentication()
        try:
            access_token = self._authentication_service.get_authentication_token(auth)
        except InvalidAuthenticationError:
            return jsonify({"msg": "Bad username or password"}), 401

        return jsonify(access_token=access_token), 200


