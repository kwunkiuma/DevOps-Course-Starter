import os
import pymongo
from todo_app.data.item import Item

def get_items():
    client = pymongo.MongoClient(os.getenv('COSMOSDB_PRIMARY_CONNECTION_STRING'))
    collection = client.todo_db.todo_items
    items = []
    for row in collection.find():
        print("reading row")
        items.append(row)
        print(row)
    return Item.from_db_items(items)

def add_item(new_item):
    client = pymongo.MongoClient(os.getenv('COSMOSDB_PRIMARY_CONNECTION_STRING'))
    collection = client.todo_db.todo_items
    new_item = {
        "name": new_item,
        "status": "To Do"
    }

    collection.insert_one(new_item).inserted_id

def move_item(id, new_list):
    client = pymongo.MongoClient(os.getenv('COSMOSDB_PRIMARY_CONNECTION_STRING'))
    collection = client.todo_db.todo_items
    collection.update_one(
        {"_id": id}, {"$set": {"status": new_list}}
    )
