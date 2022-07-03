items = [
    ("Buku", 15000),
    ("Pensil", 5000),
    ("Pulpen", 10000),
]

# list comprehensions is [expressions for item in i]

# prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]
print(sorted(prices))


# filtered = list(filter(lambda item: item[1] >= 7500, items))
filtered = [item[1] for item in items if item[1] >= 7500]
print(sorted(filtered))
