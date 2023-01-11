from todo_app.authentication.user import READER, WRITER


class ViewModel:
    def __init__(self, items, role=READER):
        self._items = items
        self._role = role

    def items_filtered_by_status(self, status):
        return [item for item in self._items if item.status == status]

    @property
    def items(self):
        return self._items

    @property
    def to_do_items(self):
        return self.items_filtered_by_status("To Do")

    @property
    def doing_items(self):
        return self.items_filtered_by_status("Doing")

    @property
    def done_items(self):
        return self.items_filtered_by_status("Done")

    @property
    def is_writer(self):
        return self._role == WRITER
