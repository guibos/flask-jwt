from flask import Blueprint

from application.use_cases.auth.views.login import LoginView
from domain.service.authentication.authentication import AuthenticationService

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')
auth_blueprint.add_url_rule('/login', view_func=LoginView.as_view('login', AuthenticationService()), methods=['GET'])
