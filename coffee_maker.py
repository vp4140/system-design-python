


"""
The coffee vending machine should support different types of coffee, such as espresso, cappuccino, and latte.
Each type of coffee should have a specific price and recipe (ingredients and their quantities).
The machine should have a menu to display the available coffee options and their prices.
Users should be able to select a coffee type and make a payment.
The machine should dispense the selected coffee and provide change if necessary.
The machine should track the inventory of ingredients and notify when they are running low.
The machine should handle multiple user requests concurrently and ensure thread safety.
"""
import time
from enum import Enum

class CoffeeType(Enum):

    CAPACHINNO = "Capachinno"
    EXPRESSO = "Expresso"

from abc import ABC,abstractmethod
class Coffee(ABC):
    def __init__(self,name,price,ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
class Capachinno(Coffee):
    def __init__(self):
        super().__init__("Capachinno",500, {"Milk":10,"Coffee":10})
class Expresso(Coffee):
    def __init__(self):
        super().__init__("Express",400, {"Milk":20,"Coffee":10})

class CoffeeFactory:
    @staticmethod
    def create_coffee(coffee_type):
        if coffee_type == CoffeeType.EXPRESSO:
            return Expresso()
        elif coffee_type == CoffeeType.CAPACHINNO:
            return Capachinno()
        else:
            raise ValueError("Invalid coffee type selected!")
from threading import Lock

class Inventory:
    def __init__(self,ingredients):
        self.ingredients = ingredients
        self.lock = Lock()


    def check_availability(self,coffee:Coffee):
        for ingredient,val in coffee.ingredients.items():
            if self.ingredients.get(ingredient,0)<val:
                return False
        return True
    def update_inventory(self,coffee):
        """
        Remove ingredients after making coffee
        :param coffee:
        :return:
        """
        for ingredient, required_qty in coffee.ingredients.items():
            self.ingredients[ingredient] -= required_qty
        pass
    def notify(self):
        for ingredient, quantity in self.ingredients.items():
            if quantity<50:
                print(f"Insufficient ingredient for {ingredient}")
class PaymentProcessing:
    def pay(self,payed,actual):
        # pei
        if payed<actual:
            print(f"Insufficient amount is paaid")
            return False,0
        return True,payed-actual
class CoffeeMachine:
    _instance = None
    menu = set([])
    def __init__(self):
        if CoffeeMachine._instance is not None:
            raise Exception("THis is a singleton Class")
        else:
            CoffeeMachine._instance = self
            self.inventory = Inventory({"Milk":100,"Sugar":100,"Coffee":100})
            self.payment_processor = PaymentProcessing()
    @staticmethod
    def get_instance():
        if CoffeeMachine._instance is None:
            CoffeeMachine()
        CoffeeMachine.create_coffee()
        return CoffeeMachine._instance
    @staticmethod
    def display_menu():
        for ele in CoffeeMachine.menu:
            print(ele.name +""+str(ele.price))

    @staticmethod
    def create_coffee():
        for ele in CoffeeType:
            obj= CoffeeFactory.create_coffee(ele)
            CoffeeMachine.menu.add(obj)
    def order_coffee(self,coffee_type,paid_amount):
        coffee = CoffeeFactory.create_coffee(coffee_type)

        # Check inventory
        if not self.inventory.check_availability(coffee):
            print(f"❌ Sorry, {coffee.name} cannot be prepared due to insufficient ingredients.")
            return

        # Process payment
        success, change = self.payment_processor.pay(paid_amount,coffee.price)
        if not success:
            return

        # Prepare Coffee
        print(f"💰 Payment successful! Preparing your {coffee.name}...")
        time.sleep(2)


        # Update inventory
        self.inventory.update_inventory(coffee)
        self.inventory.notify()

        # Provide change
        if change > 0:
            print(f"Here is your change: ${change:.2f}")
        print(f"✅ Enjoy your {coffee.name}! ☕")

def customer_order(coffe_type,paid_amount):
    coffee_machine = CoffeeMachine.get_instance()
    coffee_machine.order_coffee(coffe_type,paid_amount)
import threading
if __name__ == "__main__":
    coffee_machine = CoffeeMachine.get_instance()
    coffee_machine.display_menu()

    # Simulating concurrent orders
    threads = [
        # threading.Thread(target=customer_order, args=(CoffeeType.ESPRESSO, 5.0)),
        threading.Thread(target=customer_order, args=(CoffeeType.CAPACHINNO, 600)),
        threading.Thread(target=customer_order, args=(CoffeeType.EXPRESSO, 8.0)),
        threading.Thread(target=customer_order, args=(CoffeeType.EXPRESSO, 7.0)),
        # threading.Thread(target=customer_order, args=(CoffeeType.ESPRESSO, 4.0)),  # Insufficient payment
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
