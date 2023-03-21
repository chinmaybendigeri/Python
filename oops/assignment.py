from math import sqrt


#  Create a class Line to accepts two coordinates(x, y) as tuples and return the slope and distance
class Line:

    def __init__(self, cord1, cord2):
        self.cord1 = cord1
        self.cord2 = cord2

    def distance(self):  # distance = square_root((y2 - y1)2 + (x2 - x1)2)
        return sqrt((self.cord1[0] - self.cord2[0]) ** 2 + (self.cord1[1] - self.cord2[1]) ** 2)

    def slope(self):  # slope = y2 - y1 / x2 - x1
        return (self.cord2[1] - self.cord1[1]) / (self.cord2[0] - self.cord1[0])


line = Line((3, 2), (8, 10))

print(line.slope())
print(line.distance())


# create a class Cylinder and calculate the volume  of a Cylinder

class Cylinder():

    pi = 3.14

    def __init__(self,radius=1,height = 1):
        self.radius = radius
        self.height = height

    def volume(self):
        return (self.radius ** 2) * Cylinder.pi * self.height


cylinder = Cylinder(3, 2)
print(cylinder.volume())
