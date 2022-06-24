from email.policy import default
import pytest
from todo_app.data.item import Item
from todo_app.view_models.view_model import ViewModel

@pytest.fixture
def default_items():
    return [
        Item(1, 'To Do item', 'To Do'),
        Item(2, 'Doing item', 'Doing'),
        Item(3, 'Done item', 'Done')
    ]

def test_should_filter_to_do_items(default_items):
    # Arrange
    items = default_items

    # Act
    result = ViewModel(items).to_do_items
    assert result == [ default_items[0] ]

def test_should_filter_doing_items(default_items):
    # Arrange
    items = default_items

    # Act
    result = ViewModel(items).doing_items
    assert result == [ default_items[1] ]

def test_should_filter_to_do_items(default_items):
    # Arrange
    items = default_items

    # Act
    result = ViewModel(items).done_items
    assert result == [ default_items[2] ]