"""
python encapsulation used to hide and restrict public data
"""

class Bank:
    def __init__(self,pin,password):
        print ("welcome to the Xyz bank")
        self.pin=pin
        self.password=password
        self.__balance=10000 #encapsulation
    
    def balance(self):
        return self.__balance
    


obj=Bank(1234,"xyz")
#Access private via getter
print(obj.balance())