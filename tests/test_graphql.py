from graphene.test import Client
from api import schema
import pytest

@pytest.fixture
def client():
    client = Client(schema.schema)
    return client

def test_user_name_repos(snapshot, client):
    snapshot.assert_match(client.execute('''{ user{name repos} }''')) 

def test_user_name(snapshot, client):
    snapshot.assert_match(client.execute('''{ user{name} }''')) 