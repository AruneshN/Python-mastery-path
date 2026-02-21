"""
Topics: Class and objects

desc:
1)oops allowing you to structure your code and reusability
2)better maintaince
3)clean and structure code


"""

#class and objects
"""
class is a blue print of the objects. objects is a instance create from that blueprint.

example:
class is a car| objects is a volvo,audi
1)Dunder method - __str__ and __int__ used for human redability for easy understanding 
"""
class car: #class 
    def __init__(self,name,price): # constructor runs automatically
        #self - self used to refer the currect instance of the class The self parameter is a reference to the current instance of the class. and used to access the properties and methods.
        print("welcome car showroom")
        self.name=name
        self.price=price

    def __str__(self): #string representation
        return self.name
    
    def __int__(self): #integer representaion
        return self.price
    


obj=car("bmw",50000) # instance of the car - object for calling constructor 

print(obj,int(obj)) #show output using print without __str__ they show memory of the obj
