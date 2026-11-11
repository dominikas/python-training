def display_investigation_message():
    print("investigate activity")


application_status = "potential concern"
email_status = "okay"

if application_status == "potential concern":
    print("application_log:")
    display_investigation_message()

if email_status == "potential concern":
    print("email log:")


# Labs
# Task 2

# Define a function named `alert()`
def alert():
    print("Potential security issue. Investigate further.")

# Call the `alert()` function
alert()


# Task 3

# Define a function named `alert()`
def alert():
    for i in range(3):
        print("Potential security issue. Investigate further.")


# Call the `alert()` function
alert()


# Task 4, 5
# Define a function named `list_to_string()`

def list_to_string():
    # Store the list of approved usernames in a variable named `username_list`
    username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza", "alevitsk", "wjaffrey"]
    # Write a for loop that iterates through the elements of `username_list` and displays each element
    for name in username_list:
        print(name)


# Call the `list_to_string()` function
list_to_string()


# Task 6

# Define a function named `list_to_string()`
def list_to_string():
    # Store the list of approved usernames in a variable named `username_list`
    username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza", "alevitsk", "wjaffrey"]

    # Assign `sum_variable` to an empty string
    sum_variable = ""

    # Write a for loop that iterates through the elements of `username_list` and displays each element
    for name in username_list:
        sum_variable = sum_variable + name

    # Display the value of `sum_variable`
    print(sum_variable)


# Call the `list_to_string()` function
list_to_string()

# Task 7

# Define a function named `list_to_string()`
def list_to_string():

    # Store the list of approved usernames in a variable named `username_list`

    username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza", "alevitsk", "wjaffrey"]

    # Assign `sum_variable` to an empty string

    sum_variable = ""

    # Write a for loop that iterates through the elements of `username_list` and displays each element

    for name in username_list:
        sum_variable = sum_variable + name + ","

    # Display the value of `sum_variable`
    print(sum_variable)

# Call the `list_to_string()` function
list_to_string()