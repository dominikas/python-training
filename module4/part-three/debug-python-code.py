# Scenario
"""
In your work as a security analyst, you need to apply debugging strategies to ensure your code works properly.
"""
from module1.variables import username_list

# Task 1

# For loop that iterates over a range of numbers
# and displays a message each iteration

"""
    for i in range(10)
                      ^
SyntaxError: expected ':'
"""

for i in range(10):
    print("Connection cannot be established")

# Task 2
# Assign `usernames_list` to a list of usernames
"""
    usernames_list = ["djames", "jpark", "tbailey", "zdutchma "esmith", "srobinso", "dcoleman", "fbautist"]
                                                                                                         ^
SyntaxError: unterminated string literal (detected at line 23)
"""
usernames_list = ["djames", "jpark", "tbailey", "zdutchma", "esmith", "srobinso", "dcoleman", "fbautist"]
# Display `usernames_list`
print(usernames_list)

# Task 4
# Display a message in upper case
"""
    print("update needed".upper()
         ^
SyntaxError: '(' was never closed
"""
print("update needed".upper())

# Task 4

"""
    if name = username:
       ^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
"""

"""
    for name in username_list:
                ^^^^^^^^^^^^^
NameError: name 'username_list' is not defined. Did you mean: 'usernames_list'?
"""
# Assign `usernames_list` to a list of usernames that represent approved users
usernames_list = ["djames", "jpark", "tbailey", "zdutchma", "esmith", "srobinso", "dcoleman", "fbautist"]

# Assign `username` to a specific username
username = "esmith"

# For loop that iterates over the elements of `usernames_list` and determines whether each element corresponds to an approved user
for name in usernames_list:
    # Check if `name` matches `username`
    # If it does match, then display a message accordingly
    if name == username:
        print("The user is an approved user")

# Task 5
"""
    if username == usernames_list[5]:
                   ~~~~~~~~~~~~~~^^^
IndexError: list index out of range
"""
# Assign `usernames_list` to a list of usernames
usernames_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Assign `username` to a specific username
username = "eraab"

# Determine whether `username` is the final username in `usernames_list`
# If it is, then display a message accordingly
if username == usernames_list[len(usernames_list)-1]:
    print("This username is the final one in the list.")

# Task 6
"""
    with open(import_file, "r") as file
                                       ^
SyntaxError: expected ':'
"""
"""
    ip_addresses = split.ip_addresses()
                   ^^^^^
NameError: name 'split' is not defined
"""
# Assign `import_file` to the name of the text file
import_file = "allow_list.txt"

# Assign `remove_list` to a list of IP addressess that are no longer allowed to access the network
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# With statement that reads in the text file and stores its contents as a list in `ip_addresses`
with open(import_file, "r") as file:
    ip_addresses = file.read()

# Convert `ip_addresses` from a string to a list
ip_addresses = ip_addresses.split()

# For loop that iterates over the elements in `remove_list`,
# checks if each element is in `ip_addresses`,
# and removes each element that corresponds to an IP address that is no longer allowed

for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

# Display `ip_addresses` after the removal process
print(ip_addresses)

# Task 7
# logic error
# Assign `system` to a specific operating system as a string
system = "OS 2"

# Assign `patch_schedule` to a list of patch dates in order of operating system
patch_schedule = ["March 1st", "April 1st", "May 1st"]

# Conditional statement that checks which operating system is stored in `system` and displays a message showing the corresponding patch date
if system == "OS 1":
    print("Patch date:", patch_schedule[0])

elif system == "OS 2":
    print("Patch date:", patch_schedule[1])

elif system == "OS 3":
    print("Patch date:", patch_schedule[3])