'''
Can you change the self-parameter inside a class to something else (say 
“harry”). Try changing self to “slf” or “harry” and see the effects. 
'''

from random import randint
class Train:
    def __init__(harry, TrainNo): # even if we change the self parameter it would still work given that 
        harry.TrainNo = TrainNo  # this lines self parameter is also changed

    def book (self, fro, to):
        print(f"ticket is booked in trainNo {self.TrainNo}, from {fro} To {to}")

    def status (self):
        print(f"Tain No {self.TrainNo} is running on time")

    def fare (self, fro, to):
        print(f"the fare from {fro} To {to} is {randint(300, 1000)}")

a = Train(4579)
a.book("Raipur","Hyderabad")
a.status()
a.fare("Raipur", "Hyderabad")
        