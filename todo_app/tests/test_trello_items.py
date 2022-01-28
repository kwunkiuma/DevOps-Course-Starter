import pytest
from todo_app.data.item import Item

@pytest.fixture
def to_do_trello_list():
    return {
        'name': 'To Do',  
        'cards': [
            {
                'id': '11',
                'name': 'to do 1'
            },
            {
                'id': '12',
                'name': 'to do 2'
            }
        ]
    }

@pytest.fixture
def doing_trello_list():
    return {
        'name': 'Doing',  
        'cards': [
            {
                'id': '21',
                'name': 'doing 1'
            },
            {
                'id': '22',
                'name': 'doing 2'
            }
        ]
    }

@pytest.fixture
def done_trello_list():
    return {
        'name': 'Done',  
        'cards': [
            {
                'id': '31',
                'name': 'done 1'
            },
            {
                'id': '32',
                'name': 'done 2'
            }
        ]
    }

def test_should_retrieve_all_items(to_do_trello_list, doing_trello_list, done_trello_list):
    # Arrange
    trello_lists = [to_do_trello_list, doing_trello_list, done_trello_list]

    # Act
    result = Item.from_trello_lists(trello_lists)
    assert len(result) == 6