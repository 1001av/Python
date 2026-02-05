class employee:
    language = "python"
    salary = 1200000

    def __init__(self, name, salary, language):  # dundar method which is automatically called
        # you have to call each attribute here also
        self.name = name
        self.salary = salary
        self.language = language
        print("i am creating an object")

    def getInfo(self):  # hm koi bhi method bnaye hme self dena hota hai chahe hm use use kre ya na kre
        print(f"Language is {self.language}. The salary is {self.salary}")

    @staticmethod 
    def greet ():
        print("good morning")

# here object/inheritance is created by name akhil and it is given attributes like name,salary & language
Akhil = employee("Akhil", 1300000, "Javascript") 
# Akhil.name = "Akhil"
print(Akhil.name, Akhil.salary, Akhil.language)
# Akhil.__init__()
Akhil.getInfo()
