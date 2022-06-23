items = [
    ("Buku", 15000),
    ("Pensil", 5000),
    ("Pulpen", 10000),
]

prices = list(map(lambda item: item[1], items))
print(sorted(prices))

# map function same as like this
prices = []
for item in items:
    prices.append(item[1])

print(sorted(prices))
