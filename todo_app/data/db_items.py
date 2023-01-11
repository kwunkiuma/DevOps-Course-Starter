import os

import pymongo
from bson import ObjectId

from todo_app.authentication.login import requires_writer
from todo_app.data.item import Item


def get_items():
    client = pymongo.MongoClient(os.getenv("COSMOSDB_PRIMARY_CONNECTION_STRING"))
    collection = client.todo_db.todo_items
    items = []
    for row in collection.find():
        items.append(row)
    return Item.from_db_items(items)


@requires_writer
def add_item(new_item):
    client = pymongo.MongoClient(os.getenv("COSMOSDB_PRIMARY_CONNECTION_STRING"))
    collection = client.todo_db.todo_items
    new_item = {"name": new_item, "status": "To Do"}

    collection.insert_one(new_item).inserted_id


@requires_writer
def move_item(id, new_list):
    client = pymongo.MongoClient(os.getenv("COSMOSDB_PRIMARY_CONNECTION_STRING"))
    collection = client.todo_db.todo_items
    collection.update_one({"_id": ObjectId(id)}, {"$set": {"status": new_list}})
