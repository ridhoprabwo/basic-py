from operator import le


letters = ["a", "b", "c", "d"]

# Add
letters.append("b")
print(letters)

# Add specific position
letters.insert(2, "a")
print(letters)

# Remove by index
letters.pop(0)
print(letters)

# Remove by first occurrence of the value
letters.remove("b")
print(letters)

# Remove items by range
del letters[0:2]
print(letters)

# Remove all object in list
letters.clear()
print(letters)
