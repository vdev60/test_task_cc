from app import app
import pytest


@pytest.fixture
def client():
    return app.test_client()


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_post_request(client):
    response = client.post("/")
    assert response.status_code == 200
