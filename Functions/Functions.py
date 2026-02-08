'''
Topics:Function
Desc: Function is a block of code execute when we call.

return - is a keyword return the value back
1) function
2)keyword function - with parameter and without
3)arbitary function
4)keyword arbitary function
5)return
6) recursion
'''

#1️⃣ function - normal

def greeting(): 
    print("hello")

greeting() # function name

#2️⃣ keyword function - with parameter


def user(name,salary,role):
    print(name)
    print(role)
    print(salary)
    

user(name="arunesh",role='Developer',salary=25000)

#3️⃣arbitary function
'''
Desc: if you dont know how many times arguement will pass the function add * in parameter
'''

def calculations(*num):
    return sum(num)
print(calculations(5,8,90,6))


#4️⃣ return
"""
Desc: return is a keyword send value back to the function called

real life scenarion:
if i click button that return the values in api
"""

def values(*nums):
    return sum(nums)

value=values(10,20,35,90)
print("return :",value)




#5️⃣keyword arbitary function
"""
Desc: pass number of arguemnt with keywords
"""

def user_info(**details):
    for key,values in details.items():
        print(f"{key} ={values}")

user_info(name="Arunesh",age=22,Role="Developer",salary=25000)


