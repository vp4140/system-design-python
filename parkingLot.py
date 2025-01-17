from collections import defaultdict

from tenacity import retry_if_result


class Parking_spot:
    is_spot_parked = False
    def __init__(self,spot_id:str,vehicle_type:int):
        self.spot_id = spot_id
        self.vehicle_type = vehicle_type

    def is_parked(self,):
        return self.is_spot_parked
    def park_vehicle(self):
        self.is_spot_parked = True
    def unpark_vehicle(self):
        self.is_spot_parked = False


class Floor:
    check_free_spots={}

    def __init__(self,floor_id, parking_floor:list[list[Parking_spot]],vehicle_types):

        self.floor_id = floor_id
        self.parking_spots = [[None for i in range(len(parking_floor[0]))] for i in range(len(parking_floor))]
        self.check_free_spots = defaultdict(int)

        for ele in vehicle_types:
            self.check_free_spots[ele] = 0

        ROWS = len(parking_floor)
        COLS = len(parking_floor[0])


        for r in range(ROWS):
            for c in range(COLS):
                if parking_floor[r][c] !=0:
                    vehicle_type = parking_floor[r][c].vehicle_type
                    self.parking_spots[r][c] = Parking_spot(str(floor_id+r+c),vehicle_type)
                    self.check_free_spots[vehicle_type] +=1
    def park(self,vehicle_type):
        if self.check_free_spots(vehicle_type)!=0:
            for row in self.parking_spots:
                for spot in row:
                    if spot is not None and not spot.isparked() and spot.vehicle_type == vehicle_type:
                        self.check_free_spots[vehicle_type] -=1
                        spot.park_vehicle()

                        return spot.spot_id
        return ""