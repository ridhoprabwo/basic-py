# we can use set to remove duplicate numbers, for example
# set is unordered, can't access them using index
numbers = [1, 2, 2, 3, 1, 2, 3, 4]
first = set(numbers)
second = {2, 3, 5}

# we can union them (OR)
print(first | second)

# we can intersection them (AND)
print(first & second)

# we can get different from them
print(first - second)

# we can use XOR
print(first ^ second)
