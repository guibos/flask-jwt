from base64 import b64encode
from typing import Dict

import pytest
from flask.testing import FlaskClient

from main import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def _get_headers(username: str, password: str, client: FlaskClient) -> Dict[str, str]:
    auth_string = f"{username}:{password}".encode('utf-8')
    encoded = b64encode(auth_string).decode('utf-8')
    response = client.get("/auth/login", headers={"Authorization": f"Basic {encoded}"})
    return {"Authorization": f"Bearer {response.json['access_token']}"}


@pytest.fixture()
def user_headers(client: FlaskClient) -> Dict[str, str]:
    return _get_headers('user', 'pass', client)


@pytest.fixture()
def admin_headers(client: FlaskClient) -> Dict[str, str]:
    return _get_headers('admin', 'admin', client)

