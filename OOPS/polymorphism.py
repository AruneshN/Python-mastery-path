"""
topics:polymorphism
1)Method overriding
2)method overloading

desc:
polymorphism means many forms same method using many forms

pay is a same object but different behaviour
"""
class payment:
    def __init__(self):
        print("select payment method")
    

class UPI(payment):
    def pay(self):
        return "payment with upi"

class card(payment):
    def pay(self):
        return "payment with card"
    


u=UPI()
c=card()

for payments in (u,c):
    print(payments.pay())




#Method overriding
"""
Dis:
having multiple methods in same name but different parameter and different signature of using
pay have same name but different parameters

"""

class Payment:
    def pay(self,amount): #parent class behaviour
        return f'Processing payment {amount} is paided due to generic method'
    
class UPI(Payment):
    def pay(self,amount): #overriding
        return f'Processing payment {amount} is paided due to UPI'
    
class Net_Banking(Payment):
    def pay(self,amount):#overriding
        return f'Processing payment {amount} is paided due to Net_Banking'

class GPAY(Payment):
    def pay(self,amount):#overriding
        return f'Processing payment {amount} is paided due to Gpay'

Pay=UPI()
print(Pay.pay("25000"))


#Method overloading
"""
Method overloading is same class same name but different parameters.
add is a same name same function but receive different parameters
"""

class Calculator:
    def add(self,*nums):
        return sum(nums)


total=Calculator()
print(total.add(4,6))
print(total.add(4,6,20))
