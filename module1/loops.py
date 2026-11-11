# for loops
for i in ["elarson", "bmoreno", "tshah", "sgilmore"]:
    print(i)

### Looping through a list

computer_assets = ["laptop1", "desktop20", "smartphone03"]
for asset in computer_assets:
    print(asset)

###
string = "security"
for character in string:
    print(character)

## using range()
for i in range(0, 10, 2):
    print(i)

###
for i in range(5):
    print(i)

### while loops
i = 1
while i < 5:
    print(i)
    i = i + 1

### Integers in the loop condition
login_attempts = 0
while login_attempts < 5:
    print("Login attempts:", login_attempts)
    login_attempts = login_attempts + 1

### Boolean values in the loop condition
count = 0
login_status = True
while login_status:
    print("Try again.")
    count = count + 1
    if count == 4:
        login_status = False

### break
computer_assets = ["laptop1", "desktop20", "smartphone03"]
for asset in computer_assets:
    if asset == "desktop20":
        break
    print(asset)

### continue
computer_assets = ["laptop1", "desktop20", "smartphone03"]
for asset in computer_assets:
    if asset == "desktop20":
        continue
    print(asset)

### Labs - Create loops
# You're working as a security analyst,
# and you're writing programs in Python to automate displaying messages
# regarding network connection attempts, detecting IP addresses that are attempting
# to access restricted data, and generating employee ID numbers for a Sales department.

# Task 1
# Iterative statement using `for`, `range()`, and a loop variable of `i`
# Display "Connection could not be established." three times

for i in range(3):
    print("Connection could not be established.")

# Task 2
# Create a variable called `connection_attempts` that stores the number of times the user has tried to connect to the network

connection_attempts = 5

# Iterative statement using `for`, `range()`, a loop variable of `i`, and `connection_attempts`
# Display "Connection could not be established." as many times as specified by `connection_attempts`

for i in range(connection_attempts):
    print("Connection could not be established")

# Task 3
# Assign `connection_attempts` to an initial value of 0, to keep track of how many times the user has tried to connect to the network

connection_attempts = 0

# Iterative statement using `while` and `connection_attempts`
# Display "Connection could not be established." every iteration,
# until connection_attempts reaches a specified number

while connection_attempts < 5:
    print("Connection could not be established")
    # Update `connection_attempts` (increment it by 1 at the end of each iteration)
    connection_attempts = connection_attempts + 1

# Task 4
# Assign `ip_addresses` to a list of IP addresses from which users have tried to
# log in

ip_addresses = ["192.168.142.245", "192.168.109.50",
                "192.168.86.232", "192.168.131.147",
                "192.168.205.12", "192.168.200.48"]

# For loop that displays the elements of `ip_addresses` one at a time

for ip in ip_addresses:
    print(ip)

# Task 5
# Assign `allow_list` to a list of IP addresses that are allowed to log in

allow_list = ["192.168.243.140", "192.168.205.12",
              "192.168.151.162", "192.168.178.71",
              "192.168.86.232", "192.168.3.24",
              "192.168.170.243", "192.168.119.173"]

# Assign `ip_addresses` to a list of IP addresses from which users have tried to log in

ip_addresses = ["192.168.142.245", "192.168.109.50",
                "192.168.86.232", "192.168.131.147",
                "192.168.205.12", "192.168.200.48"]

# For each IP address in the list of IP addresses from which users have tried to log in,
# If it is among the allowed addresses, then display “IP address is allowed”
# Otherwise, display “IP address is not allowed”

for ip in ip_addresses:
    if ip in allow_list:
        print("IP address is allowed")
    else:
        print("IP address is not allowed")

# Task 6
# Assign `allow_list` to a list of IP addresses that are allowed to log in

allow_list = ["192.168.243.140", "192.168.205.12",
              "192.168.151.162", "192.168.178.71",
              "192.168.86.232", "192.168.3.24",
              "192.168.170.243", "192.168.119.173"]

# Assign `ip_addresses` to a list of IP addresses from which users have tried to log in

ip_addresses = ["192.168.86.232", "192.168.142.245",
                "192.168.109.50", "192.168.131.147",
                "192.168.205.12", "192.168.200.48"]

# For each IP address in the list of IP addresses from which users have
# tried to log in,
# To achieve this, use the break keyword and expand the message that is displayed to the user when their IP address is not in allow_list to provide more specifics. Instead of "IP address is not allowed", display "IP address is not allowed. Further investigation of login activity required".

for ip in ip_addresses:
    if ip in allow_list:
        print("IP address is allowed")
    else:
        print("IP address is not allowed. Further investigation of login activity required")
        break

# Task 7
# You have been asked to create employee IDs for a Sales department,
# with the criteria that the employee IDs should all be numbers
# that are unique, divisible by 5, and falling between 5000 and 5150.
# The employee IDs can include both 5000 and 5150.

# Assign the loop variable `i` to an initial value of 5000

i = 5000

# While loop that generates unique employee IDs for the Sales department by
# iterating through numbers
# and displays each ID created

while 5000 <= i <= 5150:
    print("ID: ", i)
    i=i+5

# Task 8
# You would like to incorporate a message that displays
# `Only 10 valid employee ids remaining` as a helpful alert once the loop variable reaches `5100`.

# Assign the loop variable `i` to an initial value of 5000

i = 5000

# While loop that generates unique employee IDs for the Sales department by iterating through numbers
# and displays each ID created
# This loop displays "Only 10 valid employee ids remaining" once `i` reaches 5100

while i <= 5150:
    print(i)
    if i==5100:
        print("Only 10 valid employee ids remaining")
    i = i + 5