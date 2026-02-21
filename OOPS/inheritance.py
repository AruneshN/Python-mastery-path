"""
Topics : inheritance
Types:
1) Single Inheritance

2) Multiple Inheritance

3) Multilevel Inheritance

4) Hierarchical Inheritance

5) Hybrid Inheritance

desc:
inheritance used for using parents class in child
"""

"""
| Type         | Structure                  |
| ------------ | -------------------------- |
| Single       | 1 Parent → 1 Child         |
| Multiple     | Multiple Parents → 1 Child |
| Multilevel   | Chain (A → B → C)          |
| Hierarchical | 1 Parent → Many Children   |
| Hybrid       | Combination                |


"""

# single inheritance
class Car:
    def __init__(self, model, year, price, type):
        self.model = model
        self.year = year
        self.price = price
        self.type = type

    def discounts(self):
        return "this feb we give 10% discount"

class ElectricCar(Car):
    def __init__(self, model, year, price, type, battery):
        super().__init__(model, year, price, type) # super keyword used to acess constructor and methods of the parents class
        self.battery = battery
        self.offer=super().discounts()


e = ElectricCar("Tesla", 2024, 5000000, "EV", "100kWh")

print(e.model)
print(e.battery)
print(e.offer)


#multiple inheritance
'''
multiple parents single child
'''
class Camera:
    def click(self):
        return "Photo taken"

class Phone:
    def call(self):
        return "Calling..."

class Computer:
    def compute(self):
        return "Processing..."

class SmartPhone(Camera, Phone, Computer):
    pass


s = SmartPhone()

print(s.click())
print(s.call())
print(s.compute())

#multilevel

"""
Each level inheritance have previous one 
"""
class Person:
    def info(self):
        return "Basic person info"

class Student(Person):
    def study(self):
        return "Studying"

class GraduateStudent(Student):
    def research(self):
        return "Doing research"


g = GraduateStudent()

print(g.info())
print(g.study())
print(g.research())

#Hierachical inheritance
"""
one parent multiple children
"""
# Hierarchical Inheritance
# One Parent -> Multiple Children

class Employees:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return "Employee is working"


class Developer(Employees):
    def code(self):
        return "Developer is writing code"


class TeamLead(Employees):
    def manage(self):
        return "Team Lead is managing the team"


# Creating objects
dev = Developer("Arunesh", 50000)
lead = TeamLead("Kumar", 80000)

print(dev.name)
print(dev.work())   # inherited method
print(dev.code())   # own method

print(lead.name)
print(lead.work())  # inherited method
print(lead.manage()) # own method

# Hybrid Inheritance Example

class Person:
    def details(self):
        return "Basic person details"


# Hierarchical part
class Employee(Person):
    def work(self):
        return "Employee working"


class Student(Person):
    def study(self):
        return "Student studying"


# Multiple inheritance part
class Intern(Employee, Student):
    def role(self):
        return "Intern role"


# Object
i = Intern()

print(i.details())  # from Person
print(i.work())     # from Employee
print(i.study())    # from Student
print(i.role())     # own method