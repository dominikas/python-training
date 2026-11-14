### Import files into Python
# Opening & Reading files in Python

# with open("update_log.txt", "r") as file:
#     updates = file.read()
#
# print("File content:", updates)

# Writing files in Python
line = "jrafael,192.168.243.140,4:56:27,True"
#
# with open("access_log.txt", "a") as file:
#     file.write(line)

### Work with files in Python
## Parsing
# .split()
approved_users = "elarson,bmoreno,tshah,sgilmore,eraab"
print("before .split():", approved_users)

approved_users = approved_users.split(",")
print("after .split():", approved_users)
#
removed_users = "wjaffrey jsoto abernard jhill awilliam"
print("before .split():", removed_users)

removed_users = removed_users.split()
print("after .split():", removed_users)

# Applying .split() to files
# with open("update_log.txt", "r") as file:
#     updates = file.read()
# updates = updates.split()
# print("file after .split():", updates)

# .join()
approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
print("before .join():", approved_users)

approved_users = ",".join(approved_users)
print("after .join():", approved_users)

# Applying .join() to files
# with open("update_log.txt", "r") as file:
#     updates = file.read()
# updates = updates.split()
# updates = " ".join(updates)
# with open("update_log.txt", "w") as file:
#     file.write(updates)

# Labs
# Task 1
"""
In this task, you'll import a security log text file and store it as a string to prepare it for analysis. 
"""
# Task 2
"""
Now, you'll use the `.read()` method to read the imported file, 
and you'll store the result in a variable named `text`. 
Afterwards, display the `text` and explore what it contains by running the cell.
"""
# Task 3
"""
The output in the previous step is one big string. 
In this task, you'll explore how you can split the string that contains the entire imported log file into a list of strings, one string per line. 
"""
# Assign `import_file` to the name of the text file that contains the security log file
import_file = "login.txt"

# First line of the `with` statement
# Use `open()` to import security log file and store it as a string
with open(import_file, "r") as file:
    # Use `.read()` to read the imported file and store the result in a variable named `text`
    text = file.read()

# Display the contents of `text`

print("File content:", text.split())

# Task 4
"""
There is a missing entry in the log file. 
You'll need to account for that by appending it to the log file. 
You're given the missing entry stored in a variable named `missing_entry`. 
"""
# Assign `missing entry` to a log that was not recorded in the log file
missing_entry = "\njrafael,192.168.243.140,4:56:27,2022-05-09"

# Use `open()` to import security log file and store it as a string
# Pass in "a" as the second parameter to indicate that the file is being opened for appending purposes

# with open(import_file, "a") as file:
#     # Use `.write()` to append `missing_entry` to the log file
#     file.write(missing_entry)
#
# # Use `open()` with the parameter "r" to open the security log file for reading purposes
# with open(import_file, "r") as file:
#     # Use `.read()` to read in the contents of the log file and store in a variable named `text`
#     text = file.read()
#
# # Display the contents of `text`
# print("After adding missing entry", text)

# Task 5
"""
The next task you're responsible for is creating a text file. 
This text file should include a list of IP addresses that are allowed to access restricted information. 
Documenting this in a text file will help you communicate your findings to your security team. 
"""
# Task 6
"""
Your next goal is to create a `with` statement in order to write the IP addresses to the text file you created in the previous step. 
"""
# Task 7
"""
In this final step, you'll complete the code you've been writing up to this point. 
You'll add code to read the file containing IP addresses.
"""
# Assign `import_file` to the name of the text file that you want to create
import_file = "allow_list.txt"

# Assign `ip_addresses` to a list of IP addresses that are allowed to access the restricted information
ip_addresses = "192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 192.168.60.153 192.168.96.200 192.168.247.153 192.168.3.252 192.168.116.187 192.168.15.110 192.168.39.246"

# Display `import_file`
print("File name:", import_file)

# Display `ip_addresses`
print("IP addresses:", ip_addresses)

# Create a `with` statement to write to the text file
with open(import_file, "w") as file:
    # Write `ip_addresses` to the text file
    file.write(ip_addresses)

# Create a `with` statement to read in the text file
with open(import_file, "r") as file:
    # Read the file and store the result in a variable named `text`
    text = file.read()

# Display the contents of `text`
print("Saved ips:", text)
