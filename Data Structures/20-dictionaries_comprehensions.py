# dictionaries comprehension
# [expression for item in items]
# comprehensions we can use for sets, list and dictionaries


# list
values = []
for x in range(5):
    values.append(x * 2)
print(values)

# we can use comprehensions
values = [x*2 for x in range(5)]
print(values)


# sets
values = {x*2 for x in range(5)}
print(values)


# dictionaries
values = {}
for x in range(5):
    values[x] = x*2
print(values)

# we can use comprehensions
values = {x: x*2 for x in range(5)}
print(values)
