import abc
from abc import ABC, abstractmethod
#first base class 
class figures(ABC):
    def __init__(self,name):
        self.n = name
    @abstractmethod
    def length_sides(self):
        pass
#second base class 
class areas(ABC):
    @abstractmethod
    def area(self):
        pass
    
class square(figures,areas):
    def __init__(self,name,side):
        super().__init__(name)
        self.s = side
    def length_sides(self):
        return self.s
    def area(self):
        self.a = self.s**2
        return self.a

s = square("square",5)
print("the name of the figure is",s.n)
print("the length of each side is ",s.length_sides())
print("the area of the figure is",s.area())