from typing import Dict

from flask.testing import FlaskClient


def test_get_post(client: FlaskClient):
    response = client.get('/blog/post/1')
    assert response.json == {'description': 'Description 1', 'post_id': 1, 'title': 'Title 1'}
    assert response.status_code == 200


def test_get_post_not_found(client: FlaskClient):
    response = client.get('/blog/post/2')
    assert response.status_code == 404


def test_delete_posts(client: FlaskClient, admin_headers: Dict[str, str]):
    response = client.delete('/blog/post/1', headers=admin_headers)
    assert response.status_code == 204


def test_delete_posts_unauthorized(client: FlaskClient):
    response = client.delete('/blog/post/1')
    assert response.status_code == 401


def test_delete_posts_unauthorized_user_auth(client: FlaskClient, user_headers: Dict[str, str]):
    response = client.delete('/blog/post/1', headers=user_headers)
    assert response.status_code == 401

