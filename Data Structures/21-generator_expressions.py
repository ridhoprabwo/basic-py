# size of generator object
from sys import getsizeof

# generator expressions, has no length, don't store all items in memory
values = (x * 2 for x in range(10))
print("gen: ", getsizeof(values))
# generator object are iterable, can iterate over them, in each iteration
# print(values)
# for x in values:
#     print(x)
