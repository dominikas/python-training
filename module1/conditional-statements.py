status = 222
if status == 100 or status == 102:
    print("informational resp")
elif status == 200 and status <= 226:
    print("successful response")
elif status == 400:
    print("Bad request")
elif status == 500:
    print("Internal server error")
else:
    print("check other status")

# Labs
# You are asked to help automate the process of checking whether a user's operating system requires an update.

# Task 1

# Assign a variable named `system` to a specific operating system, represented as a string
# This variable indicates which operating system is running
# Feel free to run this cell multiple times; each time try assigning `system` to different values ("OS 1", "OS 2", "OS 3") and observe the result

system = "OS 2"

# If OS 2 is running, then display a "no update needed" message

if system == "OS 2":
    print("no update needed")

# Task 2
# Assign `system` to a specific operating system
# This variable represents which operating system is running
# Feel free to run this cell multiple times; each time try assigning `system` to different values ("OS 1", "OS 2", "OS 3") and observe the result

system = "OS 1"

# If OS 2 is running, then display a "no update needed" message

if system == "OS 2":
    print("no update needed")

# Task 3
# Assign `system` to a specific operating system
# This variable represents which operating system is running

system = "OS 3"

# If OS 2 is running, then display a "no update needed" message
# Otherwise, display a "update needed" message

if system == "OS 2":
    print("no update needed")
else:
    print("update needed")

# Task 4
# Assign `system` to a specific operating system
# This variable represents which operating system is running

system = "OS 4"

# If OS 2 is running, then display a "no update needed" message
# Otherwise if OS 1 is running, display a "update needed" message
# Otherwise if OS 3 is running, display a "update needed" message

if system == "OS 2":
    print("no update needed")
elif system == "OS 1":
    print("update needed")
elif system == "OS 3":
    print("update needed")

# Task 5
# Assign `system` to a specific operating system
# This variable represents which operating system is running

system = "OS 3"

# If OS 2 is running, then display a "no update needed" message
# Otherwise if either OS 1 or OS 3 is running, display a "update needed" message

if system == "OS 2":
    print("no update needed")
elif system == "OS 1" or system == "OS 3":
    print("update needed")

# Task 6
# Assign `approved_user1` and `approved_user2` to usernames of approved users

approved_user1 = "elarson"
approved_user2 = "bmoreno"

# Assign `username` to the username of a specific user trying to log in

username = "bmoreno1"

# If the user trying to log in is among the approved users,
# then display a message that they are approved to access this device
# Otherwise, display a message that they do not have access to this device

if username == approved_user1 or username == approved_user2:
    print("This user has access to this device.")
else:
    print("This user does not have access to this device.")

# Task 7
# Assign `approved_list` to a list of approved usernames

approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Assign `username` to the username of a specific user trying to log in

username = "eraab1"

# If the user trying to log in is among the approved users, then display a message that they are approved to access this device
# Otherwise, display a message that they do not have access to this device

if username in approved_list:
    print("This user has access to this device.")
else:
    print("This user does not have access to this device.")

# Task 8
# Assign `organization_hours` to a Boolean value that represents
# whether the user is trying to log in during organization hours

organization_hours = True

# If the entered `organization_hours` has a value of True,
# then display "Login attempt made during organization hours."
# Otherwise, display "Login attempt made outside of organization hours."

if organization_hours:
    print("Login attempt made during organization hours.")
else:
    print("Login attempt made outside of organization hours.")

# Task 9

# Task 10
# Assign `approved_list` to a list of approved usernames

approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Assign `username` to the username of a specific user trying to log in

username = "bmoreno"

# Assign `organization_hours` to a Boolean value that represents whether the user is trying to log in during organization hours

organization_hours = True

# If the user is among the approved users
# and they are logging in during organization hours,
# then convey that the user is logged in
# Otherwise, convey that either the username is not approved
# or the login attempt was made outside of organization hours

if username in approved_list and organization_hours:
    print("Login attempt made by an approved user during organization hours.")
else:
    print("Username not approved or login attempt made outside of organization hours.")



