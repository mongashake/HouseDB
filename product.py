import uuid


class Product:
    def __init__(self, attrs):
        self.id = self.generate_id()
        self.attrs = attrs
        for k, v in attrs.items():
            setattr(self, k, v)

    @staticmethod
    def generate_id():
        return uuid.uuid1()

