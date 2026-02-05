'''
 Create a class “Programmer” for storing information of few programmers 
working at Microsoft. 
'''

class Programmer:
    company = "Google"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

p = Programmer ("Akhil", 120000, 12847628)
print(p.name, p.salary, p.pincode, p.company)