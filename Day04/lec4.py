#1. Classes
#container/blueprint to define properties , functions need to be applied for that properties

#define class
class Employeee:
#    pass

#2. Objects
#object from class
# emp = Employeee()  #reserve new place in memory so, you can add properties to the object in the runtime
# print(type(emp))
#
# emp.name = 'ahmed'
# emp.salary = 100
# emp.address = 'cairo'
#
# print(emp)
# print(emp.salary)
#
# emp2= Employeee()
# emp3= Employeee()
#
# emp2.firstname = 'zahwa'
# emp2.salary = 1000
#
# emp3.dept = 'python'
# emp3.name = 'noha'
#
# print(type(emp), type(emp2), type(emp3))
#
# print(emp.__dict__)
# print(emp2.__dict__)
# print(emp3.__dict__)

#all objects of same class must have the same properties / structure
# how object is created / to control object creation
#3. By constructor
# function __init__ ? initialize the object in memory / reserve addresss for object in memory
# you can assign properties? --> __self__
# __self__ --> bt3br 3n kol addressl ay new object being intialized

    # def __init__(self, name, email, salary):
    #     self.name = 'new'
    #     self.email = 'new@new'
    #     self.salary = 100

# emp = Employeee("ahmed", "ahmed@iti", 1000)
# print(emp.name)

#from last print it returns data intialized in constructor so, we need instance variables
#3. Instance variables / methods

#     def __init__(self, name, email, salary):
#         self.name = name
#         self.email = email
#         self.salary = salary
#
# emp = Employeee("ahmed", "ahmed@iti", 1000)
# print(emp.name)

#4. Class Variable
# property represent class not object
# can add shared property between all instances
    no_of_employees = 0
    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.salary = salary
        Employeee.no_of_employees += 1

print(Employeee.no_of_employees)   #0
emp = Employeee("ahmed", "ahmed@iti", 1000)
print(Employeee.no_of_employees)   # 1

