#OOP Concepts

#1. Inheritance
#All classes inherits from base class "object"

class Parent:
    def __init__(self, name):
        print("I am a parent object")
        self.name = name

    def print_name(self):
        print(f"My name is {self.name}")

class Child(Parent):
    def __init__(self, name):
        super().__init__(name) # call parent constructor
        print("I am a child object")

c = Child("Ahmed")
c.print_name()
