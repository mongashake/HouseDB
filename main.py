import json
from index import InvertedIndex
from inventory import Inventory
from query_engine import QueryEngine


class Main:
    def __init__(self):
        self.inventory = Inventory()
        self.index = InvertedIndex()
        self._engine = None

    @property
    def engine(self):
        if self._engine is None:
            self._engine = QueryEngine(self)
        return self._engine

    def add_product(self, attrs):
        p = self.inventory.add_product(attrs)
        self.index.update_index(p)
        return p

    def query(self, q):
        return json.dumps(self.engine.query(q))
