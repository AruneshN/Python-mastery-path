"""
Topics : Custom error handling
Desc: we can raise own exception 
1) Raise
2)assert
"""

#1️⃣ we can raise the error
"""
desc:raise handle run time error
"""

# try:
#     age = int(input("Enter your age: "))
# except ValueError:
#     raise ValueError("Custom Error: Please enter a valid number")
# else:
#     print(age)


#write a program not allowed negative value
# x=-1

# if x<0:
#     raise Exception("value Must be possitive")


#Real-time scenario: Password must have a keyword
class PasswordError(Exception):
    """Custom exception for invalid passwords"""
    pass

def check_password(password):
    if len(password) < 8:
        raise PasswordError("Password must be at least 8 characters long.")
    if "Arunesh" not in password:
        raise PasswordError("Password must contain the keyword 'Arunesh'.")
    return True

try:
    pwd = input("Enter your password: ")
    check_password(pwd)
    print("Password is valid!")

except PasswordError as e:
    print(f"Error: {e}")

#2️⃣ assert
age = int(input("Enter your age: "))

# Assert that age is at least 18
assert age >= 18, "Not eligible for vote"

print("Eligible for vote")
