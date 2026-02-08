"""
Topic : Exception handling
Desc:Error handling is handle the error during Programm run
try:
    code
except Someexception:
    code
else:
    code
finaaly:
    code
---------------------------------------------------------------
try:
    # Code that might cause an exception
except SomeError:
    # Handle exception
else:
    # Runs only if no exception happened
finally:
    # Runs always
"""

# try:
#     age = int(input("Enter your age: "))
# except ValueError:
#     print("Age should be a number")
# else:
#     print("Your age is:", age)
# finally:
#     print("Program closed")

# ------------------------------------------------------------------------------------------
"""
try:
    username = input("Enter your username: ")
    if not username:
        raise ValueError("Username cannot be empty!")

    age = int(input("Enter your age: "))
    if age <= 0:
        raise InvalidAgeError("Age must be positive!")
    if age < 18:
        raise InvalidAgeError("You must be at least 18 years old!")

except ValueError as ve:
    print("Value Error:", ve)

except InvalidAgeError as iae:
    print("Age Error:", iae)

else:
    # This runs only if no exception occurs
    print(f"Registration successful! Welcome, {username} (Age: {age})")

finally:
    print("Thank you for using our registration system.")

"""

