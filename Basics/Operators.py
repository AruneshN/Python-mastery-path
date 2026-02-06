
"""
Topics: Operators 
Description: Python operator is perform operation between vales and variables
1. Arithmetic Operators
2. Comparison (Relational) Operators
3. Logical Operators
4. Assignment Operators
5. Bitwise Operator
6. Membership Operators
7. Identity Operators
"""
#1️⃣ Arithmetic Operators
'''Arithmetic Operators is perform mathamatic operation
| Operator | Meaning        | Example |
| -------- | -------------- | ------- |
| +        | Addition       | a + b   |
| -        | Subtraction    | a - b   |
| *        | Multiplication | a * b   |
| /        | Division       | a / b   |
| %        | Modulus        | a % b   |
| **       | Power          | a ** b  |
| //       | Floor Division | a // b  |

'''
# addition
a,b=10,25
print(a+b)

# Subtraction
print(a-b)

#multiplication
print(a*b)

#division
print(a/b)

#modulus
print(a%b) #Remainder = Dividend - (Divisor × Quotient)
            # Remainder = 10 -(25 x 0)
            #remainder =10 - 0


#2️⃣ Comparison (Relational) Operators
'''
Description: Comparison operators used to compare values.Return True or False
'''
'''
| Operator | Meaning          | Example         |
| -------- | ---------------- | --------------- |
| `==`     | Equal            | `5 == 5` → True |
| `!=`     | Not Equal        | `5 != 3` → True |
| `>`      | Greater          | `5 > 3`         |
| `<`      | Less             | `5 < 3`         |
| `>=`     | Greater or Equal | `5 >= 5`        |
| `<=`     | Less or Equal    | `5 <= 6`        |

'''

# ==
print(5==4+1)

#!=
print(5!=7)

#> and <

print(5>4 and 8<10)
#<= or >=
print(5>=4 and 10<=25)


#3️⃣Logical Operators
'''
Description: perform multiple conditions in single expressions: real time examples is password and username are correct page will be login
'''
'''
| Operator | Meaning                      |
| -------- | ---------------------------- |
| `and`    | Both conditions must be True |
| `or`     | Any one condition True       |
| `not`    | Reverse condition            |

'''
# and
"""
Task: Login page
""" 
# user_name=input("enter user name:")
# password=int(input("enter password:"))

# if user_name == "Arunesh" and password == 5488:
#     print("login successful")
# else:
#     print("login failed")

## or

# day = "Sunday"

# if day == "Saturday" or day == "Sunday": # Checks if the day is Saturday OR Sunday
#     print("It's the weekend!")
# else:
#     print("It's a weekday.")

# Not
"""
username = "" # The input would go here, an empty string is False in a boolean context

if not username: # Reverses the boolean value of username (False becomes True)
    print("Username is required.")
else:
    print("Username provided.")

"""
#4️⃣ Assignment Operators
"""
Used to assign values.
"""

"""
| Operator | Example  |
| -------- | -------- |
| `=`      | `a = 10` |
| `+=`     | `a += 5` |
| `-=`     | `a -= 5` |
| `*=`     | `a *= 5` |
| `/=`     | `a /= 5` |
"""

#5️⃣ Bitwise Operator
"""
Description: bitwise operator used to we work directly on binary data.

"""
'''
| Operator | Meaning     |    |
| -------- | ----------- | -- |
| `&`      | AND         |    |
| `        | `           | OR |
| `^`      | XOR         |    |
| `~`      | NOT         |    |
| `<<`     | Left shift  |    |
| `>>`     | Right shift |    |

'''
# & - two bits are true return value or else return False
var1=2 #0010
var2=3 #0011

"""
0 | 0 | 1 | 0 
0 | 0 | 1 | 1
--------------
0 | 0 = 0 # both is zero so zero
0 | 0 =0
1 | 1 =1 # Both is true so 1
0 | 1 = 0
"""
print(var1&var2)
# | - one bits are ture return Value
print(var1|var2)

# ^ - XOR
"""
if both value have different return True.
"""
#-----------------------------------------------

#6️⃣ Membership Operator
"""
Description: Check the value inside collection. check the sequence presented in the object


in 
not in
"""
#in
# User=input("Enter Employee name:")
# Emp=["arunesh","hari","preem","john"]

# if User in Emp:
#     print(f"welcome {User}")
# else:
#     print("Sorry You dont have access!")

#not in
# if User not in Emp:
#     Emp.append(User)

# else:
#     print("already registered")
# print(Emp)


#7️⃣ Identity Operators
"""
Description: Two objects have same memory not value

Where Used
-------------------------
API response checking

Database results

Optional function parameters

is
is not
"""

database=None
if database is None:
    print("database is empty")

Api=None

if Api is None:
    print("Api failed")
