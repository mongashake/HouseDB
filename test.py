from main import Main


products = [
    {'product': 'id1', 'category': 'book', 'subCategory': 'education', 'price': 200, 'size': 10},
    {'product': 'id2', 'category': 'book', 'subCategory': 'crime', 'price': 100, 'size': 10},
    {'product': 'id3', 'category': 'book', 'subCategory': 'horror', 'price': 200, 'size': 10},
    {'product': 'id5', 'category': 'book', 'subCategory': 'horror', 'price': 100, 'size': 5},
    {'product': 'id6', 'category': 'movie', 'subCategory': 'horror', 'price': 200, 'size': 5},
    {'product': 'id7', 'category': 'movie', 'subCategory': 'education', 'price': 200, 'size': 10},
]

inter = Main()
for product in products:
    inter.add_product(product)

q = {'filter': {'category': 'book'}}
print(inter.query(q))

q = {'filter': {'category': 'book', 'price': 200}, 'groupedBy': 'subCategory'}
print(inter.query(q))

q = {'filter': {'category': 'book'}, 'groupedBy': 'price_range'}
print(inter.query(q))
