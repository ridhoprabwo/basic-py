from distutils.command.build_scripts import first_line_re


numbers = [1, 2, 3, 4, 4, 4, 5, 2, 4, 6]

# unpacking list with other on last item
first, second, *other = numbers

print(first)
print(second)
print(other)


# unpacking list between first and last item
first, *between, last = numbers
print(first)
print(between)
print(last)
