# Add a static method in problem 2, to greet the user with hello. 

class Calculator:
    def __init__(self, n):
        self.n = n

    @staticmethod
    def greet ():
        print("Hello, Chaliye shuru krte hai")

    def Square (self):
        print(f"The square is {self.n * self.n}")

    def Cube (self):
        print(f"The cube is {self.n * self.n * self.n}")

    def SquareRoot (self):
        print(f"The square root is {self.n ** 1/2}")

a = Calculator(4)
a.greet()
a.Square()
a.Cube()
a.SquareRoot()