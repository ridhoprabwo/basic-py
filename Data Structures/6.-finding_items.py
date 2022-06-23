from itertools import count


letters = ["a", "b", "c"]
# find index of value, if doesn't exist in list, that return is error
print(letters.index("c"))

if "d" in letters:
    print(letters.index("d"))


letters.append("c")

count_letter = letters.count("g")
print(count_letter)
