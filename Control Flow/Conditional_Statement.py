"""
Topics:
Description: Control statement is a program control the flow of execution, which code run how mnay times run.
1) Conditional statement - Decision Making
    1) if else
    2)elif
    3)nested if and elif

2) Loop Control Statement
    1) For loop
    2) While Loop
    3)nested loop

3) LooP Control Keywords
    1)pass
    2)break
    3)continue
"""

#1️⃣ Conditional statement-Decision Making
'''
1) if - else
Desc: if statement run when Condition is True.Else statement run if condition failed.
'''
age=18

if age >=18:
    print("Eligible for Vote")
else:
    print(" You are under age")

lst=[3,7,9,10]
result=[x for x in lst if x>6]
#2️ elif
'''
Desc: elif - is a statement if previous condition failed elif run
'''
mark=99

if mark>=90:
    print("Graded A")
elif mark>=70:
    print("Grade B")
else:
    print("Grade c")

#3️ Nested if and elif
"""
Desc: Nested statement used make multiple flow of control in if inside if and elif
"""
Mark=70
attendance=91-10
if mark >=50:
    print("pass")
    if attendance >=88:
        print("Eligible for Next round")
    else:
        print("attendance failed")
elif mark>=35:
    print("retest required")

else:
    print("failed")

#2️⃣ Loop control statement
'''
1) for
2) while
'''

#1) for
'''
Desc: for loop is a control statement loop execute number of iteration already knowns.if you know how mant times code want to execute use for loop.
real times scenarion:
1) bulk email sending 
2) billing software

'''
for i in range(1,11):
    print(f'{i} x 2 = {i*2}')

#1) Bulk email sending 
mail=["aruneshnataraj@gamil.com","nadhini@gmail.com","swetha@gmail.com"]

for Mail in mail:
    print("Sending email to",Mail)

"comprehension list"
odd=[x for x in range(1,20) if x%2 !=0]
print(odd)


#2) while loop
'''
while loop used dont know how many times loop was  executed. loop executed until condition failed
real time example:
1) login system - if user enter wrong password authentication ask password again 
2) gaming loop
3) Atm - pin verification - enter wrong pin ask again
'''

# gamming loop - find number 1 to 7 if i find correct game i win else i failed 3 times game will be lost
#library
import random

live=3 #life span
score=0
# while live >0:
#     num=random.randint(3,10)
#     guess=int(input("Enter Gueesed number:"))

#     if guess == num:
#         score +=10
#         print("you win ")
        
#     else:
#         live-=1
#         print(f'Your guess number is {guess} - actual number {num}')
# print("game over your score :", score)

# 3) Nested loop 
"""
1) Nested loop used for loop inside another loop
"""

# Task- Student mark list
#work all students multiple iteratons in same time
# students={
#     "Arunesh":[70,80,65,79,99],
#     "hari":[78,100,99,74,100],
#     "jeus":[100,100,31,80,100]
# }

# for name,marks in students.items():
#     print("students",name)
#     for mark in marks:
#         print("Marks",mark)


#3️⃣ Loop Control Keyword
'''
1)Pass - pass do nothing this is a place holder of uncompleted code
2)break - exit the loop of currect iterations 
3)continue -Skip the iteration ( best and used for filteration)
'''


#1)Pass - place holder
def feature():
    pass

#2)break
"""
break used for exit the loop example i want to print on
"""
# friends=["arunesh","hari","seeni","gopi","sweetha"]
# for lst in friends:
#     print("checking:",lst)
#     if lst=="seeni":
#         print("stop the loop seeni was founded")
#         break
#     print(lst)

# for i in range(10):
#     if i ==6:
#         break
#     print(i)  

#2) continue- continue skip the interation of the program - best for filtering
"""
filter the member who have afe greater than or equal 24
"""
db={
    "arunesh":23,
    "hari":24,
    'gokul':29,
    "john":16,
    "sweetha":17,
    "gopi":21,
    "ajith":36,
    "prem":20
}

for name,age in db.items():
    if age >=24:
        continue
    print(name)