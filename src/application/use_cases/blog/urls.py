from flask import Blueprint

from application.use_cases.blog.views.post import PostView
from domain.service.authentication.authentication import AuthenticationService
from domain.service.blog.service import BlogService

blog_blueprint = Blueprint('blog', __name__, url_prefix='/blog')
blog_blueprint.add_url_rule('/post/<int:post_id>', view_func=PostView.as_view('post', BlogService(), AuthenticationService()), methods=['GET', 'DELETE'])
