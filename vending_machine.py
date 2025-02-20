"""
The vending machine should support multiple products with different prices and quantities.
The machine should accept coins and notes of different denominations.
The machine should dispense the selected product and return change if necessary.
The machine should keep track of the available products and their quantities.
The machine should handle multiple transactions concurrently and ensure data consistency.
The machine should provide an interface for restocking products and collecting money.
The machine should handle exceptional scenarios, such as insufficient funds or out-of-stock products.



Coin
val qnatity
Notes;
val qnatity
Money:
 Notes
 Coins


Product:
    prodduct_id
    producr_quantitup
    :type



Machine:
    machine_id
    # numbr_of uniquw proiducts

    Prodict [] = [

    get product:
        change logic
        add_product
User:
    usr_id
    user_name

The Product class represents a product in the vending machine, with properties such as name and price.
The Coin and Note enums represent the different denominations of coins and notes accepted by the vending machine.
The Inventory class manages the available products and their quantities in the vending machine. It uses a concurrent hash map to ensure thread safety.
The VendingMachineState interface defines the behavior of the vending machine in different states, such as idle, ready, and dispense.
The IdleState, ReadyState, and DispenseState classes implement the VendingMachineState interface and define the specific behaviors for each state.
The VendingMachine class is the main class that represents the vending machine. It follows the Singleton pattern to ensure only one instance of the vending machine exists.
The VendingMachine class maintains the current state, selected product, total payment, and provides methods for state transitions and payment handling.
The VendingMachineDemo class demonstrates the usage of the vending machine by adding products to the inventory, selecting products, inserting coins and notes, dispensing products, and returning change.
"""
from enum import Enum
class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
class Coin(Enum):
    PENNY = 0.01
    NICKEL = 0.05
    DIME = 0.1
    QUARTER = 0.25
class Note(Enum):
    ONE = 1
    FIVE = 5
    TEN = 10
    TWENTY = 20
class Inventory:
    def __init__(self):
        self.products = {}
    def get_product_quantity(self,product):
        return self.products[product]
    def add_product(self,product,quantity):
        self.products[product] = quantity
    def remove_product(self,product):
        del self.products[product]
    def is_available(self, product):
        return product in self.products and self.products[product] > 0

from abc import ABC,abstractmethod
class VendingMachineState(ABC):

    @abstractmethod
    def select_product(self, product):
        pass

    @abstractmethod
    def insert_coin(self, coin):
        pass

    @abstractmethod
    def insert_note(self, note):
        pass

    @abstractmethod
    def dispense_product(self):
        pass

    @abstractmethod
    def return_change(self):
        pass
from threading import Lock


class ReadyState:
    pass
class IdealState:
    pass
class DispenseState:
    pass


class VendingMachine:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            cls._instance = super().__new__(cls)

            cls._instance  = Inventory()
            cls._instance = ReadyState(cls._instance)
            cls._instance = IdealState()
            cls._instance = DispenseState()


class add_product_state(VendingMachineState):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine
    def select_product(self, product):
        # if self.vending_machine
        pass
    def insert_coin(self, coin):
        print("first Select products")


    def insert_note(self, note):
        print("first Select products")

    def dispense_product(self):
        print("first Select products")
    def return_change(self):
        print("first Select products")
