### Working with variables in functions

# Parameters
def remaining_login_attempts(maximum_attempts, total_attempts):
    print("remaining_login_attempts:", maximum_attempts - total_attempts)

# Arguments

remaining_login_attempts(3, 2)

# Return statements

def remaining_login_attempts(maximum_attempts, total_attempts):
    return  maximum_attempts - total_attempts

remaining_attempts = remaining_login_attempts(3, 3)
if remaining_attempts <= 0:
    print("Your account is locked")

### Global and local variables

# Global variables
device_id = "7ad2130bd"

# Local variables
def greet_employee(name):
    total_string = "Welcome" + name
    return total_string

#
username = "elarson"
def identify_user():
    print(username)
identify_user()

#
print("1:" + username)
def greet():
    username = "bmoreno"
    print("2:" + username)
greet()
print("3:" + username)