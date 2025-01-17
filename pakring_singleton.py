
from enum import Enum
from random import random


class VehicleType(Enum):
    CAR = 1
    MOTORCYCLE = 2
    TRUCK = 3

class Vehicle:
    def __init__(self,type:VehicleType):
        self.vehicletype = type

class Car(Vehicle):
    def __init__(self):
        super().__init__(VehicleType.CAR)

class Bike(Vehicle):
    def __init__(self):
        super().__init__(VehicleType.MOTORCYCLE)

class ParkingSpot:
    def __init__(self,spot_id):

        self.parked_vehicle = None
        self.parkingType =  VehicleType.CAR
        self.spot_id = spot_id

    def park_vehicle(self,vehicle:Vehicle):
        if self.parkingType == vehicle.vehicletype and self.parked_vehicle is None:
            self.parked_vehicle = vehicle
        else:
            raise ValueError("Invalid vehicle type")

    def unpark_vehicle(self):
        self.parked_vehicle = None
    def get_parked_vehicle(self):
        return self.parked_vehicle
    def get_spot_number(self) -> int:
        return self.spot_id

class Level:
    def __init__(self,id,room):
        self.id = id
        self.room = room
        self.parking_spots = [ParkingSpot(spot_id=i) for i in range(room)]


    def park_vehicle(self,vehicle:Vehicle):
        for ele in self.parking_spots :
            if not ele.parked_vehicle and ele.parkingType == vehicle.vehicletype :
                ele.parked_vehicle= vehicle
                print("Parked on Levels")
                return True
        print("Not Parked on Levels")
        return False


    def unpark_vehicle(self,vehicle:Vehicle):
        for ele in self.parking_spots:
            if ele.get_parked_vehicle() == vehicle:
                ele.unpark_vehicle()
                return True
        return False



    def display_availability(self):
        for ele in self.parking_spots:

                available =   "   Available" if ele.parked_vehicle is None else "   Occupied"
                print(str(ele.spot_id) + available)
        print(" ")

class ParkingLot:
    #singleton class
    def __init__(self):
        self._instance= True
        self.level: list[Level] = []

    def addLevel(self,level:Level):
        self.level.append(level)

    def park_vehicle(self,vehicle:Vehicle):
        for ele in self.level:
            if ele.park_vehicle(vehicle):
                return  True
        return False

    def unpark_vehicle(self,vehicle:Vehicle):
        for ele in self.level:
            if ele.unpark_vehicle(vehicle):
                if ele.unpark_vehicle():
                    return True
        return False

    def display_availability(self):
        for ele in self.level:
            ele.display_availability()

if __name__ == "__main__":
    obj = ParkingLot()

    obj.addLevel(Level(1,10))
    obj.addLevel(Level(2, 10))
    car =Car()
    bike = Bike()


    obj.park_vehicle(car)
    obj.park_vehicle(bike)

    obj.display_availability()



