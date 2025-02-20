"""
4 components
observer,subject
oberserv concrete classes
subject concrete class
subject - stores all observers, add observer, removeobserver, notifyall observers,
setweather

oberver = update()

"""
from abc import ABC,abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self,weather:str):
        pass

class Subject:
    def setObserver(self,observer:Observer):
        pass
    def removeObserver(self,observer:Observer):
        pass
    def notifyall(self):
        pass

class Weatherapp(Subject):
    observerList = []
    weather = "None"
    def setObserver(self,observer:Observer):
        self.observerList.append(observer)

    def removeObserver(self,observer:Observer):
        self.observerList.remove(observer)

    def notifyall(self):
        for ele in self.observerList:
            ele.update(self.weather)
    def update_weather(self,weather):
        self.weather = weather
        self.notifyall()

class TV(Observer):
    weather = ""
    def update(self, weather: str):
        self.weather = weather
        self.display_weather()

    def display_weather(self):
        print("TV has " + self.weather)

class Mobile(Observer):
    weather = ""
    def update(self, weather: str):
        self.weather = weather
        self.display_weather()

    def display_weather(self):
        print("Mobile has " + self.weather)

weatherapp = Weatherapp()
observer = TV()
observer1 = Mobile()
weatherapp.setObserver(observer)
weatherapp.setObserver(observer1)
weatherapp.update_weather("Cloudy")



