## Scenario
"""
You are a security professional working at a health care company.
As part of your job, you're required to regularly update a file that identifies the employees who can access restricted content.
The contents of the file are based on who is working with personal patient records.
Employees are restricted access based on their IP address.
There is an allow list for IP addresses permitted to sign into the restricted subnetwork.
There's also a remove list that identifies which employees you must remove from this allow list.
Your task is to create an algorithm that uses Python code to check whether the allow list contains any IP addresses identified on the remove list. If so, you should remove those IP addresses from the file containing the allow list.

"""
"""
In this lab, you're working as a security analyst and you're responsible for developing an algorithm that parses a file containing IP addresses that are allowed to access restricted content and removes addresses that no longer have access.
"""
## Task 1
"""
Your eventual goal is to develop an algorithm that parses a series of IP addresses that can access restricted information and removes the addresses that are no longer allowed. Python can automate this process.
"""
# Assign `import_file` to the name of the file
import_file = "allow_list.txt"

# Assign `remove_list` to a list of IP addresses that are no longer allowed to access restricted information.
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Display `import_file`
print("Imported file content", import_file)

# Display `remove_list`
print("Remove list", remove_list)

## Task 2
"""
In this task, start by opening the text file using the `import_file` variable, the `with` keyword, and the `open()` function with the `"r"` parameter. 
"""
## Task 3
"""
Now, use the `.read()` method to read the imported file and store it in a variable named `ip_addresses`. 
"""
## Task 4
"""
After reading the file, reassign the `ip_addresses` variable so its data type is updated from a string to a list. Use the `.split()` method to achieve this. 
Adding this step will allow you to iterate through each of the IP addresses in the allow list instead of navigating a large string that contains all the addresses merged together. 
"""
## Task 5
"""
Now, you'll write code that removes the elements of `remove_list` from the `ip_addresses` list. 
This will require both an iterative statement and a conditional statement. 
"""
## Task 6
"""
Now, build a conditional statement to remove the elements of `remove_list` from the `ip_addresses` list. 
The conditional statement should be placed inside the iterative statement that loops through `ip_addresses`. 
In every iteration, if the current element in the `ip_addresses` list is in the `remove_list`, the `remove()` method should be used to remove that element. 
"""
## Task 7
"""
The next step is to update the original file that was used to create the `ip_addresses` list. 
A line of code containing the `.join()` method has been added to the code so that the file can be updated. 
This is necessary because `ip_addresses` must be in string format when used inside the `with` statement to rewrite the file.
"""
## Task 8
"""
In this task, you'll verify that the original file was rewritten using the correct list. 
"""
## Task 9
"""
The next step is to bring all of the code you've written leading up to this point and put it all into one function. 
"""
# Task 10
# Define a function named `update_file` that takes in two parameters:
# `import_file` and `remove_list`
# and combines the steps you've written in this lab leading up to this

def update_file(import_file, remove_list):
    with open(import_file, "r") as file:
        # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`
        ip_addresses = file.read()

    # Use `.split()` to convert `ip_addresses` from a string to a list
    ip_addresses = ip_addresses.split()

    # Build iterative statement
    # Name loop variable `element`
    # Loop through `ip_addresses`

    for element in ip_addresses:
        # Display `element` in every iteration
        print("Element:", element)
        if element in remove_list:
            ip_addresses.remove(element)

    print("After removal:", ip_addresses)

    # Convert `ip_addresses` back to a string so that it can be written into the text file
    ip_addresses = " ".join(ip_addresses)

    # Build `with` statement to rewrite the original file
    with open(import_file, "w") as file:
        # Rewrite the file, replacing its contents with `ip_addresses`
        file.write(ip_addresses)

# Call `update_file()` and pass in "allow_list.txt" and a list of IP addresses to be removed

update_file(import_file, remove_list)

# Build `with` statement to read in the updated file
with open(import_file, "r") as file:
    # Read in the updated file and store the contents in `text`
    text = file.read()

# Display the contents of `text`
    print("After all:", text)