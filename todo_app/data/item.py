class Item: 
    def __init__(self, id, name, status = 'To Do'): 
        self.id = id 
        self.name = name 
        self.status = status

    @classmethod 
    def from_trello_card(cls, card, list): 
        return cls(card['id'], card['name'], list['name'])

    def from_trello_list(trello_list):
        items = []
        for card in trello_list['cards']:
            items.append(Item.from_trello_card(card, trello_list))
        return items