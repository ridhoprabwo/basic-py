numbers = [1, 2, 3]
print(numbers)
# unpacking operators use asterik (*)
# we can return output unpackage list with unpacking operators,
print(*numbers)


values = list(range(5))
values = [*range(5), *"Hello"]
print(type(values))

# combine multiple list
first = [1, 2]
second = [3]
values = [*first, "a", *second, *"Hello"]
print(values)


# dictionary use two asterik (**)
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)
