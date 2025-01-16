from abc import ABC,abstractmethod

class VehicleStategy(ABC):
    @abstractmethod
    def drivecapability(self):
        pass
class OffroadStrategy(VehicleStategy):
    def drivecapability(self):
        print("OFF Raod")
class NormaDriveSrategy(VehicleStategy):
    def drivecapability(self):
        print("Normal Drive")

class Vehicle:

    def __init__(self,vs :VehicleStategy):
        self.vs = vs
    def call_drive_cpability(self):
        self.vs.drivecapability()

class OffRoadVehicle(Vehicle):
    def __init__(self):
        super().__init__(OffroadStrategy())
        # super(OffroadStrategy())

class TruckVehicle(Vehicle):
    def __init__(self):
        super().__init__(NormaDriveSrategy())

offroad = OffRoadVehicle()
offroad.call_drive_cpability()

offroad = TruckVehicle()
offroad.call_drive_cpability()

offroad = TruckVehicle()
offroad.call_drive_cpability()