from flask_login import UserMixin

WRITER = "writer"
READER = "reader"

roles = {"36454654": WRITER}


def get_role(id):
    return roles.get(id, READER)


class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.role = get_role(id)
