from abc import ABC,abstractmethod

"""
Instead of using new or directly instantiating objects, 
you delegate the creation logic to a factory method or class.

The Factory Design Pattern is a creational design pattern that provides 
a way to create objects without specifying their exact class in the client code. 
It is especially useful when you need to decide at 
runtime which subclass or object to instantiate.
"""
class Shape(ABC):
    @abstractmethod
    def draw(self,):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def draw(self):
        print(3.14*self.radius*self.radius)
class Sqaure(Shape):
    def __init__(self,side):
        self.side = side
    def draw(self):
        print(self.side* self.side)
# class Reactangle(Shape):
#     def __init__(self,length,rb):
#         self.side = side
#     def draw(self):
#         print(self.side* self.side)

# adding Factory class that holds a static method.
# Client code becomes really less
class ShapeFactory:
    @staticmethod
    def get_shape(shape_type,*args):
        if shape_type =="Circle":
            return Circle(*args)
        elif shape_type == "Square":
            return Sqaure(*args)
arr = [ ShapeFactory.get_shape("Circle",4), ShapeFactory.get_shape("Square",5)]
for ele in arr:
    ele.draw();




