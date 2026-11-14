### Strings and the security analyst
# Working with indices in strings
device_id = "h32rb17"

print("h32rb17"[0])

index_plus = 3
print("Char at index", index_plus, device_id[index_plus])

index_minus = -3
print("Char at index", index_minus, device_id[index_minus])

print("h32rb17"[0:3])

### String functions and methods

# str() and len()
device_id_length = len("h32rb17")
if device_id_length == 7:
    print("The device ID has 7 characters.")

# .upper() and .lower()
device_id = "h32rb17"
print(device_id.upper())

# .index()
print("h32rb17".index("r"))
print("r45rt46".index("r"))

# Finding substrings with .index()
tshah_index = "tsnow, tshah, bmoreno - updated".index("tshah")
print(tshah_index)

### Labs

# Task 1
"""
In your organization, employee IDs are currently either four digits or five digits
in length. In this task, you're given a four-digit numeric employee ID stored in 
a variable called `employee_id`. Convert this to a string format and store 
the result in the same variable. Later, you'll update this employee ID string 
so that it complies with a new standardized format.
"""

# Assign `employee_id` to a four digit number as an initial value
employee_id = 4186

# Display the data type of `employee_id`
print(type(employee_id))

# Reassign `employee_id` to the same value but in the form of a string
employee_id = str(employee_id)

# Display the data type of `employee_id` now
print(type(employee_id))

# Task 2
"""
Imagine that you have just been informed of a new criteria for employee IDs. 
They must all be five digits long for standardization purposes.

In this task, you will write a conditional statement that displays a message 
if the length of the employee ID is less than five digits. 
"""
# Task 3
"""
In this task, you'll build upon the previous code. 
If an employee ID is only four digits, 
you'll use concatenation to create a five-digit employee ID number.
"""

# Assign `employee_id` to a four digit number as an initial value
employee_id = 4186

# Reassign `employee_id` to the same value but in the form of a string
employee_id = str(employee_id)

# Display the `employee_id` as it currently stands
print(employee_id)

# Conditional statement that displays a message
# if the length of `employee_id` is less than five digits
if (len(employee_id)) < 5:
    print("This employee ID has less than five digits. It does not meet length requirements.")
    employee_id = "E" + employee_id

print(employee_id)

# Task 4
"""
Now you'll move on to the next part of your task. 
Imagine that the characters in a device ID convey technical information about the device. 
You'll need to extract characters in specific positions from the device ID. 
Start off by extracting the fourth character.  
"""

# Task 5
"""
Now you will also need to extract the first through the third characters in the device ID. 
So take a slice of the device ID. 
You can achieve this using bracket notation in Python. 
Then, display the slice to examine the result.
"""
# Assign `device_id` to a string that contains alphanumeric characters
device_id = "r262c36"

# Extract the first through the third characters in `device_id` and display the result
print("the first through the third characters in `device_id`", device_id[0:3])

# Task 6
"""
You'll now proceed to the last part of your task. 
This involves extracting components of a URL.
"""
# Task 7
"""
Later in this lab, you'll extract the domain extension. 
To prepare for this, use the `.index()` method to identify the index where the domain extension `.com` is located in the given URL.
"""
# Assign `url` to a specific URL
url = "https://exampleURL1.com"

# Extract the protocol of `url` along with the syntax following it, display the result
prot_end_index = url.index("://")
print("URL protocol", url[0:prot_end_index])

# Task 8
"""
It's a good idea to save important data in variables when programming. 
This allows for quick and easy tracking and reuse of information. 
"""
# Task 9
"""
You can use string slicing to also extract the domain extension of a URL. 
To do so, you can create a slice.
"""
# Task 10
"""
Finally, extract the website name from the given URL using string slicing 
and the `ind` variable that you defined earlier.
"""
# Display the index where the domain extension ".com" is located in `url`
print("the index where the domain extension", url.index(".com"))

# Assign `ind` to the output of applying `.index()` to `url` in order to extract the starting index of ".com" in `url`
ind = url.index(".com")
print("the index where the domain extension", ind)

# Extract the domain extension in `url` and display it
print("the domain extension", url[ind:ind + 4])

# Extract the website name in `url` and display it
protocol_ind_end=8
print("website name", url[protocol_ind_end:ind])
