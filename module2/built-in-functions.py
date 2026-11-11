### Built-in functions
# print()
month = "September"
print("Investigate failed login attempts during", month, "if more than", 100)

# type()
print(type("This is a string"))

# max() and min()

time_list = [12, 2, 32, 19, 57, 22, 14]
print("Min:", min(time_list))
print("Max:", max(time_list))

# sorted()

time_list = [12, 2, 32, 19, 57, 22, 14]
print("Original", time_list)
print("Sorted", sorted(time_list))
sored_list = sorted(time_list)
print("Original after sort", time_list)
print("New", sored_list)

### Labs

# Task 1
""" 
In this task, use a built-in Python function to order the list.
You'll pass the call to the function that sorts the list directly into the `print()` function.
This will allow you to display and examine the result. """

# Assign `failed_login_list` to the list of the number of failed login attempts per month

failed_login_list = [119, 101, 99, 91, 92, 105, 108, 85, 88, 90, 264, 223]

# Sort `failed_login_list` in ascending numerical order and display the result

print("Sorted list:", sorted(failed_login_list))

# Task 2

"""
Now, you'll want to isolate the highest number of failed login attempts
so you can later investigate information about the month when that highest value occurred."""

# Assign `failed_login_list` to the list of the number of failed login attempts per month

failed_login_list = [119, 101, 99, 91, 92, 105, 108, 85, 88, 90, 264, 223]

# Determine the highest number of failed login attempts from `failed_login_list` and display the result

print("The highest number of failed login attempts:", max(failed_login_list))

# Task 3, 4

"""
In your work as an analyst, you'll first define a function that displays
a message about how many login attempts a user has made that day."""

# Define a function named `analyze_logins()` that takes in two parameters,
# `username` and `current_day_logins`

def analyze_logins(username, current_day_logins):
    # Display a message about how many login attempts the user has made that day
    print("Current day login total for", username, "is", current_day_logins)

# Call `analyze_logins()`
analyze_logins("ejones", 9)


# Task 5

""" 
Now, you'll need to expand this function so that it also provides
the average number of login attempts made by the user on that day.
Doing this will require incorporating a third parameter into
the function definition. """

# Define a function named `analyze_logins()` that takes in three parameters,
# `username`, `current_day_logins`, and `average_day_logins`

def analyze_logins(username, current_day_logins, average_day_logins):
    # Display a message about how many login attempts the user has made that day
    print("Current day login total for", username, "is", current_day_logins)

    # Display a message about average number of login attempts the user has made that day
    print("Average logins per day for", username, "is", average_day_logins)


# Call `analyze_logins()`
analyze_logins("ejones", 9, 3)


# Task 6

"""
In this task, you'll further expand the function.
Include a calculation to get the ratio of the logins made on the current
day to the logins made on an average day. """

# Task 7
"""
In this task, use the `return` keyword to output the `login_ratio` from the function, 
so that it can be used later in your work. """

# Define a function named `analyze_logins()` that takes in three parameters,
# `username`, `current_day_logins`, and `average_day_logins`

def analyze_logins(username, current_day_logins, average_day_logins):
    # Display a message about how many login attempts the user has made that day
    print("Current day login total for", username, "is", current_day_logins)

    # Display a message about average number of login attempts the user has made that day
    print("Average logins per day for", username, "is", average_day_logins)

    # Calculate the ratio of the logins made on the current day to the logins made on an average day, storing in a variable named `login_ratio`
    return current_day_logins / average_day_logins


# Call `analyze_logins()`
username = "ejones"
login_analysis = analyze_logins(username, 9, 3)
# Display a message about the ratio
print(username, "logged in", login_analysis, "times as much as they do on an average day.")

# Task 8

"""
In this task, you'll use the value of `login_analysis` in a conditional statement.
When the value of `login_analysis` is greater than or equal to `3`,
then the login activity will require further investigation,
and an alert will be displayed. """

if login_analysis >= 3:
    print("Alert! This account has more login activity than normal.")
