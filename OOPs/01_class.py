# multiple objects can be created from a single class

class Employee:
   # language & salary are all class attributes because they belong to the class
    language = "python"   
    salary = 1200000

Akhil = Employee()  # here akhil is an object/ inheritance
Akhil.name = "Akhil Verma"
print(Akhil.name, Akhil.salary, Akhil.language)

harry = Employee()
harry.name = "Harry Harinder"
harry.language = "Javascript"  # the object attribute gets preference 
print(harry.name,harry.salary, harry.language)

# here name is instance attribute & salary and language are class attribute