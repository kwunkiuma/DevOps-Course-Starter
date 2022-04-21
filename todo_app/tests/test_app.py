import os
import pytest
import requests
from dotenv import load_dotenv, find_dotenv
from todo_app import app

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    test_app = app.create_app()

    with test_app.test_client() as client:
        yield client

def test_index_page(monkeypatch, client):
    monkeypatch.setattr(requests, 'get', get_lists_stub)
    response = client.get('/')
    
    assert response.status_code == 200
    assert 'To do card' in response.data.decode()

def test_add(monkeypatch, client):
# Replace call to requests.get(url) with our own function
    monkeypatch.setattr(requests, 'get', get_lists_stub)
    response = client.post('/add')
    
    assert response.status_code == 302
    
class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data
    def json(self):
        return self.fake_response_data

def get_lists_stub(url, headers, params):
    test_board_id = os.environ.get('TRELLO_BOARD_ID')
    fake_response_data = None

    if url == f'https://api.trello.com/1/boards/{test_board_id}/lists':
        fake_response_data = [{
            'id': '123abc',
            'name': 'To Do',
            'cards': [{'id': '456', 'name': 'To do card'}]
        }]
    return StubResponse(fake_response_data)
