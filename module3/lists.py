### Lists and the security analyst

# Bracket notation
username_list = ["elarson", "fgarcia", "tshah", "sgilmore"]
print("the element with an index of 2", username_list[2])
print("the element with an index of 2", ["elarson", "fgarcia", "tshah", "sgilmore"][2])

# Extracting a slice from a list
username_list = ["elarson", "fgarcia", "tshah", "sgilmore"]
print("a slice from a list", username_list[0:2])

# Changing the elements in a list
username_list = ["elarson", "fgarcia", "tshah", "sgilmore"]
print("Before changing an element:", username_list)
username_list[1] = "bmoreno"
print("After changing an element:", username_list)

# List methods
# .insert()
username_list = ["elarson", "bmoreno", "tshah", "sgilmore"]
print("Before inserting an element:", username_list)
username_list.insert(2, "wjaffrey")
print("After inserting an element:", username_list)

# .remove()
username_list = ["elarson", "bmoreno", "wjaffrey", "tshah", "sgilmore"]
print("Before removing an element:", username_list)
username_list.remove("elarson")
print("After removing an element:", username_list)

# .append()
username_list = ["bmoreno", "wjaffrey", "tshah", "sgilmore"]
print("Before appending an element:", username_list)
username_list.append("btang")
print("After appending an element:", username_list)

numbers_list = []
print("Before appending a sequence of numbers:", numbers_list)
for i in range(10):
    numbers_list.append(i)
print("After appending a sequence of numbers:", numbers_list)

# .index()
username_list = ["bmoreno", "wjaffrey", "tshah", "sgilmore", "btang"]
username_index = username_list.index("tshah")
print("Username index:", username_index)
