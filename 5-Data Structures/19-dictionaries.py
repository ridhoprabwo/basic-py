# dictionaries in python have a key and values.
# for example name as a key, had a contact as a value

point = {"x": 1, "y": 2}
# same as
point = dict(x=1, y=2)

# change value for x
point["x"] = 10
print(point)

# add more key and value in variabel point
point["z"] = 20
print(point)

# checking if key is doesn't exist or exist in variabel point, and print that values.
if "x" in point:
    print(point["x"])

# get data from key, if doesn't exist we can return 0 or anything we want, or none.
print(point.get("a", 0))

# delete some key, for example delete key "y"
del point["y"]
print(point)

# we can iterated all the key, and value
for key in point:
    print(key, ":", point[key])

# we can use funtion items, for get return as tuple and we get a key and value
print("\nUsing Items")
for key, value in point.items():
    print(key, ":", value)
