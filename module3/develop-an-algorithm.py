### Scenario
"""
In this lab, you're working as a security analyst and you're responsible for developing an algorithm that connects users to their assigned devices.
You'll write code that indicates if a user is approved on the system and has brought their assigned device to the security team.
"""
# Task 1
"""
You'll work with a list of approved usernames along with a list of the approved devices assigned to these users. The elements of the two lists are synchronized. In other words, the user at index `0` in `approved_users` uses the device at index `0` in `approved_devices`. Later, this will allow you to verify if the username and device ID entered by a user correspond to each other.
"""
# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg", "4n482ts", "a307vir"]

index = 3
# Display the element at the specified index in `approved_users`
print(approved_users[index])

# Display the element at the specified index in `approved_devices`
print(approved_devices[index])

# Task 2
"""
You'll work with a list of approved usernames along with a list of the approved devices assigned to these users. The elements of the two lists are synchronized. In other words, the user at index `0` in `approved_users` uses the device at index `0` in `approved_devices`. Later, this will allow you to verify if the username and device ID entered by a user correspond to each other.
"""

# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg", "4n482ts", "a307vir"]

# Assign `new_user` to the username of a new approved user
new_user = "gesparza"

# Assign `new_device` to the device ID of the new approved user
new_device = "3rcv4w6"

# Add that user's username and device ID to `approved_users` and `approved_devices` respectively
approved_users.append(new_user)
approved_devices.append(new_device)

# Display the contents of `approved_users`
print("Approved users:", approved_users)

# Display the contents of `approved_devices`
print("Approved devices:", approved_devices)

# Task 3
"""
An employee has left the team and should no longer have access to the system. 
"""

# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg", "4n482ts", "a307vir", "3rcv4w6"]

# Assign `removed_user` to the username of the employee who has left the team
removed_user = "tshah"

# Assign `removed_device` to the device ID of the employee who has left the team
removed_device = "2ye3lzg"

# Remove that employee's username and device ID from `approved_users` and `approved_devices` respectively
approved_users.remove(removed_user)
approved_devices.remove(removed_device)

# Display `approved_users`
print("Approved users:", approved_users)

# Display `approved_devices`
print("Approved devices", approved_devices)

# Task 4
"""
As part of verifying a user's identity in the system, you'll need to check if the user is one of the approved users. Write a conditional statement that verifies if a given username is an element of the list of approved usernames. 
"""

# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

# Assign `username` to a username
username = "sgilmore"

# Conditional statement
# If `username` belongs to `approved_users`, then display "The user ______ is approved to access the system."
# Otherwise display "The user ______ is not approved to access the system."
if username in approved_users:
    print("The username", username, "is approved to access the system.")
else:
    print("The username", username, "is not approved to access the system.")

# Task 5
"""
The next part of the algorithm uses the `.index()` method to find the index of `username` in the `approved_users` and store that index in a variable named `ind`.
"""

# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

# Assign `username` to a username
username = "sgilmore"

# Assign `ind` to the index of `username` in `approved_users`
ind = approved_users.index(username)

# Display the value of `ind`
print("Index of", username, "is:", ind)

# Task 6
"""
This task will allow you to build your understanding of list operations for the algorithm that you'll eventually build. It will demonstrate how you can find an index in one list and then use this index to display connected information in another list.
"""

# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

# Assign `username` to a username
username = "sgilmore"

# Assign `ind` to the index of `username` in `approved_users`
ind = approved_users.index(username)

# Display the device ID at the index that matches the value of `ind` in `approved_devices`
print("the device ID", approved_devices[ind])

# Task 7
"""
Your next step in creating the algorithm is to determine if a username and 
"""

# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

# Assign `username` to a username
username = "sgilmore"

# Assign `device_id` to a device ID
device_id = "4n482ts"

# Assign `ind` to the index of `username` in `approved_users`
ind = approved_users.index(username)

# Conditional statement
# If `username` belongs to `approved_users`, and if the device ID at `ind` in `approved_devices` matches `device_id`,
# then display a message that the username is approved,
# followed by a message that the user has the correct device

if username in approved_users and approved_devices[ind] == device_id:
    print("The username", username, "is approved to access the system.")
    print(device_id, "is the assigned device for", username)

# Task 8
"""
It would also be helpful for users to receive messages when their username is not approved or their device ID is incorrect.
"""
# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

# Assign `username` to a username
username = "sgilmore"

# Assign `device_id` to a device ID
device_id = "4n482ts"

# Assign `ind` to the index of `username` in `approved_users`
ind = approved_users.index(username)

# If statement
# If `username` belongs to `approved_users`, and if the element at `ind` in `approved_devices` matches `device_id`,
# then display a message that the username is approved,
# followed by a message that the user has the correct device

if username in approved_users and device_id == approved_devices[ind]:
    print("The user", username, "is approved to access the system.")
    print(device_id, "is the assigned device for", username)

    # Elif statement
    # Handles the case when `username` belongs to `approved_users` but element at `ind` in `approved_devices` does not match `device_id`,
    # and displays two messages accordingly
elif username in approved_users and device_id != approved_devices[ind]:
    print("The user", username, "is approved to access the system, but", device_id, "is not their assigned device.")

# Task 9
"""
In this task, you'll complete your algorithm by developing a function that uses some of the code you've written in earlier tasks. 
This will automate the login process.
"""
# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]


# Define a function named `login` that takes in two parameters, `username` and `device_id`
def login(username, device_id):
    # If `username` belongs to `approved_users`,

    if username in approved_users:
        # then display "The user ______ is approved to access the system.",
        print("The user", username, "is approved to access the system.")

        # assign `ind` to the index of `username` in `approved_users`,
        ind = approved_users.index(username)
        # and execute the following conditional
        # If `device_id` matches the element at the index `ind` in `approved_devices`,

        if device_id == approved_devices[ind]:
            # then display "______ is the assigned device for ______"
            print(device_id, "is the assigned device for", username)
        # Otherwise,
        else:
            # display "______ is not their assigned device"
            print(device_id, "is not their assigned device.")

    # Otherwise (part of the outer conditional and handles the case when `username` does not belong to `approved_users`),
    else:
        # Display "The user ______ is not approved to access the system."
        print("The username", username, "is not approved to access the system.")

# Call the function you just defined to experiment with different username and device_id combinations
print("login method testing")
login("elarson","8rp2k75")
login("elarson","hl0s5o1")
login("domi","8rp2k75")
