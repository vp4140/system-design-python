from typing import  List
from _datetime import datetime

class User:
    def __init__(self,id:str,name:str):
        self.user_id = id,
        self.user_name = name

class Driver:
    def __init__(self,id:str,name:str):
        self.id = id
        self.name = name

from enum import Enum

class Status(Enum):
    Requested = "Requested"
    Complete = "Complete"
    Ongoing = "Ongoing"
    Cancelled = "Cancelled"


class Ride:
    def __init__(self,rid:int,user:User,driver:Driver):
        self.rid = rid
        self.user = user
        self.driver = driver
        self.start_time = None
        self.end_time = None
        self.ride_cost = 0
    def start_ride(self):
        self.status =  Status.Ongoing
        self.start_time = datetime.now()
    def cancel_ride(self):
        self.status = Status.Cancelled
        self.end_time = datetime.now()



class RideService:
    def __init__(self):
        self.drivers ={}
        self.rides ={}
        self.ride_count = 0

    def add_driver(self,driver:Driver):
        self.drivers[driver.id] = driver

    def request_ride(self,user:User):
        pass
    



