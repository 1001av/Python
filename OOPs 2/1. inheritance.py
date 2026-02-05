class employee:
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

# class Programmer:
#    company = "ITC Infotech"
#    def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#    def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")

# we use inheritance to do the above method for reducing copy paste 

class Programmer(employee):
    company = "ITC Infotech"
    def showLanguage (self):
        print("the name is {self.name} and he is good with {self.language} language")

a = employee()
b = Programmer()
a.name = "Akhil"
a.salary = 10000
a.show()

print(a.company,b.company)