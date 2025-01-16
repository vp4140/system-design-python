from abc import ABC, abstractmethod

from matplotlib.patches import Rectangle
from rich.box import SQUARE

# Single responsibility PRoinciple

class UserManager:
    def __init__(self,userName,passWord):
        __userName = userName
        __password = passWord
    def accceptUserInfo(self,userName,password,age,etc):
        pass



#Open-Close principle
#New shapes can be added by creating new classes without modifying existing ones

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Sqaure(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side* self.side

class Reactangle2(Shape):
    def __init__(self,length,breath):
        self.length = length
        self.breath = breath
    def area(self):
        return self.length*self.breath

findall = [Sqaure(4), Reactangle2(4,3)]
for ele in findall:
    print(ele.area())


#Liskov Substitution Principle (LSP)
# This exaple breaks the principle

class Bird:
    def fly(self):
        print("I can fly")
class Sparrow(Bird):
    def fly(self):
        print("Sparrow fly")
class Chicken(Bird):
    def fly(self):
        raise NotImplementedError("Chicken cant fly")

def print_fly(obj:Bird):
    print(obj.fly())
birds = [Sparrow(),Chicken()]
for bird in birds:
    try:
        print_fly(bird)
    except NotImplementedError as e:
        print(e)

# Fixed model for liskov:

class Bird(ABC):
    @abstractmethod
    def eat(self):
        pass


class FlyingBird(Bird):
    @abstractmethod
    def fly(self):
        pass


class NonFlyingBird(Bird):
    pass


class Sparrow(FlyingBird):
    def eat(self):
        return "Sparrow is eating seeds."

    def fly(self):
        return "Sparrow is flying."


class Penguin(NonFlyingBird):
    def eat(self):
        return "Penguin is eating fish."


# Usage
def bird_actions(bird: Bird):
    print(bird.eat())
    if isinstance(bird, FlyingBird):
        print(bird.fly())


# Test cases
sparrow = Sparrow()
penguin = Penguin()

bird_actions(sparrow)  # Output: Sparrow actions including flying
bird_actions(penguin)  # Output: Penguin actions without flying


#4. Interface Segregation Principle
class Printer(ABC):
    @abstractmethod
    def printEverything(self):
        pass
class Scanner(ABC):
    @abstractmethod
    def scanEverything(self):
        pass
class MultipurposeScanner(Printer,Scanner):
    def printEverything(self):
        print("PrintEverything")

    def scanEverything(self):
        print("Scan everything")

class OnlyScanner(Scanner):
    def scanEverything(self):
        print("Scan2 Everything")


scanners = [MultipurposeScanner(),OnlyScanner()]
for ele in scanners:

    if isinstance(ele,MultipurposeScanner):
        ele.printEverything()
        ele.scanEverything()
    else:
        ele.scanEverything()



# Depencendy injection
# High-level modules should not depend on low-level modules.
# Both should depend on abstractions.

#Here, Notification depends on the abstraction MessageSender,
# making it flexible to use other senders like SmsSender.


class Sender(ABC):
    @abstractmethod
    def sendEmail(self,message):
        pass


class EmailSender(Sender):
    def sendEmail(self,message):
        print("Email Sent",message)


class Notification:
    def __init__(self,Sender):
        self.sender = Sender

    def notify(self,message):
        self.sender.sendEmail(message)

notif = Notification(EmailSender())
notif.notify("hello")






