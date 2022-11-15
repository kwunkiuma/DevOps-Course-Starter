import os
import pytest
import requests
import mongomock
import pymongo
from dotenv import load_dotenv, find_dotenv
from todo_app import app


@pytest.fixture
def client():
    file_path = find_dotenv(".env.test")
    load_dotenv(file_path, override=True)

    test_app = app.create_app()

    with test_app.test_client() as client:
        yield client


@pytest.fixture
def client():
    file_path = find_dotenv(".env.test")
    load_dotenv(file_path, override=True)
    
    with mongomock.patch(servers=(("fakemongo.com", 27017),)):
        test_app = app.create_app()
        db_client = pymongo.MongoClient("mongodb://fakemongo.com")
        objects = [
            {
                "id_": "1",
                "name": "To do card",
                "status": "To Do"
            },
            {
                "id_": "2",
                "name": "to do 2",
                "status": "To Do"
            },
            {
                "id_": "3",
                "name": "doing 1",
                "status": "Doing"
            },
            {
                "id_": "4",
                "name": "doing 2",
                "status": "Doing"
            },
            {
                "id_": "5",
                "name": "done 1",
                "status": "Done"
            },
            {
                "id_": "6",
                "name": "done 2",
                "status": "Done"
            }
        ]
        db_client.todo_db.todo_items.insert_many(objects)
        with test_app.test_client() as client:
            yield client

def test_index_page(client):
    response = client.get("/")
    
    assert response.status_code == 200
    assert "To do card" in response.data.decode()
