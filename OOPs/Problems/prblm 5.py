'''
 Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
and get fare information of train running under Indian Railways. 
'''
from random import randint
class Train:
    def __init__(self, TrainNo):
        self.TrainNo = TrainNo

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
        