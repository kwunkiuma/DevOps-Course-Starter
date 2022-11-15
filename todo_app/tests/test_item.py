import pytest
from todo_app.data.item import Item

@pytest.fixture
def db_items():
    return [
        {
            '_id': '1',
            'name': 'to do 1',
            'status': 'To Do'
        },
        {
            '_id': '2',
            'name': 'to do 2',
            'status': 'To Do'
        },
        {
            '_id': '3',
            'name': 'doing 1',
            'status': 'Doing'
        },
        {
            '_id': '4',
            'name': 'doing 2',
            'status': 'Doing'
        },
        {
            '_id': '5',
            'name': 'done 1',
            'status': 'Done'
        },
        {
            '_id': '6',
            'name': 'done 2',
            'status': 'Done'
        },
    ]

def test_should_retrieve_all_items(db_items):
    # Act
    result = Item.from_db_items(db_items)
    assert len(result) == 6