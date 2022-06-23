items = [
    ("Buku", 15000),
    ("Pensil", 5000),
    ("Pulpen", 10000),
]


filtered = list(filter(lambda item: item[1] >= 7500, items))
print(sorted(filtered, reverse=True))
