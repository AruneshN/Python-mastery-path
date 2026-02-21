"""
topics:polymorphism

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