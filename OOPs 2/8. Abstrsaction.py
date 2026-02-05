from abc import ABC, abstractmethod

class Vehicle(ABC):   # Abstract class
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with a key")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with a button")

# Using abstraction
v1 = Car()
v2 = Bike()

v1.start()   # Car starts with a key
v2.start()   # Bike starts with a button
