from collections import defaultdict


class InvertedIndex:
    PRICE_RANGE = ['200-500', '500+']

    def __init__(self):
        self._index = defaultdict(lambda: defaultdict(set))

    @property
    def index(self):
        return self._index

    def update_index(self, product):
        for k, v in product.attrs.items():
            self._index[k][v].add(product.id)
            self.index_by_price_range(product)

    def filter(self, k, v):
        return self._index[k][v]

    def get_group(self, k):
        return self._index[k]

    def index_by_price_range(self, product):
        price = getattr(product, 'price', None)
        if price is None:
            return
        if 200 <= price <= 500:
            self._index['price_range']['200-500'].add(product)
        elif price > 500:
            self._index['price_range']['500+'].add(product)
