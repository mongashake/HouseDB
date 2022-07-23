from product import Product


class Inventory:
    def __init__(self):
        self._inventory = {}

    @property
    def inventory(self):
        return self._inventory

    def add_product(self, attrs):
        p = Product(attrs)
        self._inventory[p.id] = p
        return p
