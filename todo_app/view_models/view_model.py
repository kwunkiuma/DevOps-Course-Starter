class ViewModel:
    def __init__(self, items):
        self._items = items

    def items_filtered_by_status(self, status):
        return [item for item in self._items if item.status == status]
    
    @property
    def items(self):
        return self._items
        
    @property
    def to_do_items(self):
        return self.items_filtered_by_status('To Do')

    @property
    def doing_items(self):
        return self.items_filtered_by_status('Doing')
        
    @property
    def done_items(self):
        return self.items_filtered_by_status('Done')