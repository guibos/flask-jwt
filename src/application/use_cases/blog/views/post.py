from flask import jsonify, app, make_response, request, abort
from flask.views import MethodView
from pydantic import ValidationError

from application.use_cases.auth_mixin import AuthMixin
from domain.entities.post.post_id import PostId
from domain.service.authentication.interface import AuthenticationServiceInterface
from domain.service.authorization.exceptions.unauthorized_error import UnauthorizedError
from domain.service.blog.exceptions.post_not_found_error import PostNotFoundError
from domain.service.blog.interface import BlogServiceInterface


class PostView(MethodView, AuthMixin):
    def __init__(self, blog_service: BlogServiceInterface, authentication_service: AuthenticationServiceInterface):
        self._authentication_service = authentication_service
        self._blog_service = blog_service

    def get(self, post_id: int):
        try:
            post_id_obj = PostId(post_id=post_id)
        except ValidationError:
            return {"error": "Unexpected post id"}, 400
        try:
            post = self._blog_service.get_post(post_id_obj)
        except PostNotFoundError:
            return {"error": "Not found"}, 404

        return post.model_dump(), 200

    def delete(self, post_id: int):
        try:
            post_id_obj = PostId(post_id=post_id)
        except ValidationError:
            return {"error": "Unexpected post id"}, 400

        auth = self._get_authentication()

        try:
            requester = self._authentication_service.get_data_from_token(auth)
        except UnauthorizedError:
            abort(401)

        try:
            self._blog_service.delete_post(requester=requester, post_id=post_id_obj)
        except PostNotFoundError:
            return {"error": "Post not found"}, 404
        except UnauthorizedError:
            return abort(401)

        return {}, 204


