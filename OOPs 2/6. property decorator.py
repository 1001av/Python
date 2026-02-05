class Employee:

# The @property decorator is a way to make class methods act like attributes. 
# It’s part of Python’s built-in descriptor protocol, and it’s often used to control access to instance variables while keeping a clean, attribute-like syntax.
    @property # decorator can modify a function (@property = method disguised as an attribute.)  
    def name(self):
        return f"{self.fname} {self.lname}"

# this can also be the example of encapsulation & abstraction (encapsulation - wrapping data and methods together & restricting direct access)    
# Abstraction - hiding the complex details & showing only essential features 
    @name.setter # here the method is used as an attribute 
    def name (self, value):
        self.fname = value.split(" ")  [0] # here we split the name with space which gives us first & last name
        self.lname = value.split(" ")[1] # 0 & 1 is used to describe different words in a list

# main goal to use property decorators is to return the name & the setter method is used to set the fname and lname, without the users knowledge

e = Employee()

e.name = "Harry Khan"
print(e.fname, e.lname)