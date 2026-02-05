'''
 Write a class “Calculator” capable of finding square, cube and square root of a 
number. 
'''
class Calculator:
    def __init__(self, n):
        self.n = n

    def Square (self):
        print(f"The square is {self.n * self.n}")

    def Cube (self):
        print(f"The cube is {self.n * self.n * self.n}")

    def SquareRoot (self):
        print(f"The square root is {self.n ** 1/2}")

a = Calculator(6)
a.Square()
a.Cube()
a.SquareRoot()