from base64 import b64encode

import jwt
from flask.testing import FlaskClient


def test_login(client: FlaskClient):
    encoded = b64encode(b"user:pass").decode('utf-8')
    response = client.get("/auth/login", headers={"Authorization": f"Basic {encoded}"})
    data = jwt.decode(response.json['access_token'], options={"verify_signature": False})
    assert response.status_code == 200
    assert data == {'account_id': 2, 'username': 'user', 'permissions': ['read']}


def test_login_ko(client: FlaskClient):
    encoded = b64encode(b"user:error").decode('utf-8')
    response = client.get("/auth/login", headers={"Authorization": f"Basic {encoded}"})
    assert response.status_code == 401
