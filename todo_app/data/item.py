class Item:
    def __init__(self, id, name, status="To Do"):
        self.id = id
        self.name = name
        self.status = status

    @classmethod
    def from_db_item(cls, item):
        return cls(item["_id"], item["name"], item["status"])
        return items

    def from_db_items(db_items):
        items = []
        for db_item in db_items:
            items.append(Item.from_db_item(db_item))
        return items
