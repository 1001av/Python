class employee:
    language = "python"
    salary = 1200000

    def getInfo(self):  # hm koi bhi method bnaye hme self dena hota hai chahe hm use use kre ya na kre
        print(f"Language is {self.language}. The salary is {self.salary}")

# Sometimes we need a function that does not use the self-parameter. We can define a static method like this: 
# It can be called without creating an object of the class and is mainly used for utility or helper functions.
    @staticmethod  # decorator to mark greet as a static method
    def greet ():
        print("good morning") # iske andr hme object ka kuch bhi property nhi chahiye

Akhil = employee()
Akhil.language = "Javascript"
Akhil.getInfo()              # both of these statement are same just written differently
# employee.getInfo(Akhil)   
Akhil.greet()
