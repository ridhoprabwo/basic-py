# tuple data (1, a), tuples is immutable, cannot mutate them, cannot change them or modify.

point = 1, 2
print(type(point))
# add more tuple
point1 = (3, 4, 10)
print(type(point))
added = point + point1
print(added)

print(added[0:2])

a, b, c, d, e = added
if 10 in added:
    print("exists")

# try to change value in index and get error
# point[0] = 10


# try with "Hello world", and to be tuple if assignment tuple
word = tuple("Hello World")
print(word)
