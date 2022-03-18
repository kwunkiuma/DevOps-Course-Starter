import requests
import os
from todo_app.data.item import Item

key = os.getenv('TRELLO_API_KEY')
token = os.getenv('TRELLO_API_TOKEN')
board_id = os.getenv('TRELLO_BOARD_ID')

auth_params = {
    'key': key,
    'token': token
}

def get_list_id(list_name):
    url = (f'https://api.trello.com/1/boards/{board_id}/lists')

    headers = {
        'Accept': 'application/json'
    }

    params = {
        **auth_params,
        'cards': 'open',
        'fields': 'name'
    }

    response = requests.request(
        'GET',
        url,
        headers=headers,
        params=params
    )

    for trello_list in response.json():
        if trello_list['name'] == list_name:
            return trello_list['id']

def get_items():
    url = (f'https://api.trello.com/1/boards/{board_id}/lists')

    headers = {
        'Accept': 'application/json'
    }

    params = {
        **auth_params,
        'cards': 'open',
        'fields': 'name'
    }

    response = requests.request(
        'GET',
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
        **auth_params,
        'name': new_item,
        'idList': to_do_id
    }

    requests.request(
        "POST",
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
        **auth_params,
        'idList': done_id,
    }

    requests.request(
        "PUT",
        url,
        headers=headers,
        params=query
    )