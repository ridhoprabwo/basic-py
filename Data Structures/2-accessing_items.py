letters = ["a", "b", "c", "d"]
print(letters)
# print first Item
print(letters[0])

# print first item from the end of the list
print(letters[-1])

# change item in index 0
letters[0] = "A"
print(letters)

# print item from zero to three index
print(letters[0:3])
print(letters[:3])

# print item from zero to all, same like print all
print(letters[:])

# print item every second from first index
print(letters[::2])

# print item every third from first index
print(letters[::3])


# example with numbers
numbers = list(range(20))
print(numbers[::2])
print(numbers[::3])

# reverse order with list
print(numbers[::-1])
