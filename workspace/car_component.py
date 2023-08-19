import uuid

class CarComponent:
    def __init__(self, name, uid=None):
        self.name = name
        self.uid = uid if uid else str(uuid.uuid4())
