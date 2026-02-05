class employee:
    company = "ITC"
    name = "Vidang Raina"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class Coder:
    language ="Python"
    def printLanguage(self):
        print(f"Out of all the languages here is your language: {self.language}")

class Programmer(employee,Coder):
    company = "ITC Infotech"
    def showLanguage (self):
        print(f"the name is {self.company} and he is good with {self.language} language")

a = employee()
b = Programmer()
b.show()  # in this show function is called from the class 'employee' which contains name & language
# but the language is defined in the relevant class so that dominates 
b.showLanguage()
b.printLanguage()