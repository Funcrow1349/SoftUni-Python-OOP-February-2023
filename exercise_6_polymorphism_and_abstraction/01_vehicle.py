#   Create an abstract class called Vehicle that should have abstract methods drive and refuel. Create 2 vehicles that
#   inherit the Vehicle class (a Car and a Truck) and simulates driving and refueling them. Car and Truck both receive
#   fuel_quantity and fuel_consumption in liters per km upon initialization. They both can be driven a given distance:
#   drive(distance) and refueled with a given amount of fuel: refuel(fuel). It is summer, so both vehicles use air
#   conditioners, and their fuel consumption per km when driving is increased by 0.9 liters for the car and 1.6 liters
#   for the truck. Also, the Truck has a tiny hole in its tank, and when it is refueled, it keeps only 95% of the given
#   fuel. The car has no problems and adds all the given fuel to its tank. If a vehicle cannot travel the given
#   distance, its fuel does not change.

from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: int):
        pass

    @abstractmethod
    def refuel(self, fuel: int):
        pass


class Car(Vehicle):
    CONSUMPTION_FIX = 0.9

    def drive(self, distance: int):
        if self.fuel_quantity >= distance * (self.fuel_consumption + Car.CONSUMPTION_FIX):
            self.fuel_quantity -= distance * (self.fuel_consumption + Car.CONSUMPTION_FIX)

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    CONSUMPTION_FIX = 1.6

    def drive(self, distance: int):
        if self.fuel_quantity >= distance * (self.fuel_consumption + Truck.CONSUMPTION_FIX):
            self.fuel_quantity -= distance * (self.fuel_consumption + Truck.CONSUMPTION_FIX)

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)


