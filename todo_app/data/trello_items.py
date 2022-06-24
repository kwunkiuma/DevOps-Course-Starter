import requests
import os
from todo_app.data.item import Item

def get_auth_params():
    key = os.getenv('TRELLO_API_KEY')
    token = os.getenv('TRELLO_API_TOKEN')
    return {'key': key, 'token': token}

def get_list_id(list_name):
    board_id = os.getenv('TRELLO_BOARD_ID')
    url = (f'https://api.trello.com/1/boards/{board_id}/lists')

    headers = {
        'Accept': 'application/json'
    }

    params = {
        **get_auth_params(),
        'cards': 'open',
        'fields': 'name'
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    for trello_list in response.json():
        if trello_list['name'] == list_name:
            return trello_list['id']

def get_items():
    board_id = os.getenv('TRELLO_BOARD_ID')
    url = (f'https://api.trello.com/1/boards/{board_id}/lists')

    headers = {
        'Accept': 'application/json'
    }

    params = {
        **get_auth_params(),
        'cards': 'open',
        'fields': 'name'
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    return Item.from_trello_lists(response.json())

def add_item(new_item):
    to_do_id = get_list_id('To Do')    
    url = "https://api.trello.com/1/cards"

    headers = {
        "Accept": "application/json"
    }

    query = {
        **get_auth_params(),
        'name': new_item,
        'idList': to_do_id
    }

    requests.post(
        url,
        headers=headers,
        params=query
    )
    
def move_item(id, new_list):
    url = (f'https://api.trello.com/1/cards/{id}')

    done_id = get_list_id(new_list)
 
    headers = {
        "Accept": "application/json"
    }

    query = {
        **get_auth_params(),
        'idList': done_id,
    }

    requests.put(
        url,
        headers=headers,
        params=query
    )