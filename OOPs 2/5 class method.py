class Employee:
    a = 1
    @classmethod  # this decorator is used for a method which is bound to the class and not the object of the class. 
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45
e.show() # even when we have updated the values in object, still it shows the
# original values because of class method