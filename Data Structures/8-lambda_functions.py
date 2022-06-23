items = [
    ("Buku", 15000),
    ("Pensil", 5000),
    ("Pulpen", 10000),
]

items.sort(key=lambda item: item[1],)
print(items)


# lambda function same as like this
def sort_item(item):
    return item[1]


items.sort(key=sort_item,)
print(items)
