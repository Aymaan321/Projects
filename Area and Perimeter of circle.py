import math


class Circle():
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius**2 * math.pi
    def circumfirence(self):
        return self.radius*2*math.pi

radius = int(input("What is the radius of the circle?"))
circle = Circle(radius)   
print(f"The area of the circle is {circle.area()} and the circumfirence is {circle.circumfirence()}") 
