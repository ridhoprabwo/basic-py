import re


numbers = [3, 54, 123, 49, 1, 90]

# reverse number, if values is False that can be sort
# numbers.sort(reverse=True)
# print(numbers)

# sorted number built in function
print(sorted(numbers, reverse=True))
print(numbers)


# sorting with tuple
items = [
    ("Buku", 15000),
    ("Pulpen", 10000),
    ("Pensil", 5000),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item, reverse=False)
print(items)
