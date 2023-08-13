from abc import ABC,abstractmethod
import math

class AreaCalculator:  # type: ignore
    def area(self,shape):
        if isinstance(shape,Circle):
            return math.pi*shape.radius**2
        elif isinstance(shape,Rectangle):
            return shape.width*shape.height

class Circle:# type: ignore
    def __init__(self,radius):
        self.radius = radius
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height


"""
-   Calculates the area of different shapes using conditional statements insede the AreaCalculator class.
    **  This violates the OCP -> open for extension but closed for motification.
        ***    Adding more shpaes we need to modify this class.
"""

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi*self.radius**2
class Rectangele(Shape):
    def __init__(self,width,height):
        super().__init__()
        self.widht  = width
        self.height = height
        
    def area(self):
        return self.widht*self.height
class AreaCalculator:
    def area(self,shape:Shape):
        return shape.area()
    
        
