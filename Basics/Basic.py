"""
Topic: Variables in Python
Description:
Variables are containers used to store values.
"""

# 1️⃣ Assigning a variable
a = 10
# print("Value of a:", a)


# 2️⃣ Multiple variable assignment
a, b, c = 10, 11, 12
# print(a, b, c)


# 3️⃣ Assign same value to multiple variables
x = y = z = 10
# print(x, y, z)


"""
Topic: Data Types
Description:
Data type is the type of value assigned to a variable.
"""

# 1️⃣ String
# String is a sequence of characters inside quotes
name = "Arunesh"

# 2️⃣ Integer
# int represents whole numbers
age = 22

# 3️⃣ Boolean
# Boolean represents True or False
is_adult = 7 > 6
is_minor = 4 > 5
# print(is_adult)
# print(is_minor)

# 4️⃣ Complex
# Complex number has real + imaginary part
num = complex(100)
# print(num)


"""
Topic: Type Conversion
Description:
Type conversion means converting one data type into another data type.
"""

age = "23"        # string
age = int(age)   # string → int
# print(type(age))
