import abc
from abc import ABC, abstractmethod
class Dog(ABC):
    x = "mammal"
    y = 3000
    def __init__(self,breed,colour,name):
        self.b = breed 
        self.c = colour
        self.n  = name
        
    def cost(self):
        self.food  = 1000
        self.clothes = 100
        self.total = self.food + self.clothes
    #@abstractmethod
    #now the print_results is just a template for the other methods in child class but must be instantiate. 
    def print_results(self):
        print("the breed is",self.b)
        print("the colour is",self.c)
        print("the name is ",self.n)
        print("the cost is",self.total)
class Cat(Dog):
    def __init__(self,breed,colour,name,hair_colour):
        self.h = hair_colour
        super().__init__( breed,colour,name)
    def print_hair(self):
        print("the colour of hair is ",self.h)
        print("the breed of the cat is",self.b)
        print("the colour of the cat is",self.c)
        print("the name of the cat is",self.n)
        print("the total cost is",self.total + 1000)
        print(self.food)
        print(self.clothes)
    #overriding the print_results method in the parent class using super()
    def rk(self):
        super().print_results()
        print("subclass")
    #traditional method of overriding the abstract method from the abstract parent class 
    #def print_results(self):
        #print("this cat is naughty")
c = Cat("persian","white","tom","black")
#d = Dog("labrador","black","bob")
#d.cost()
#d.print_results()
c.cost()
c.print_hair()
print(c.x)
c.rk()
#c.print_results()
