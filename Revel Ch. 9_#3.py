# Project #3:
import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self._x = x
        self._y = y
    def getx(self):
        return self._x
    def gety(self):
        return self._y
    def distance(self, other):
        return float("{:.2f}".format(math.dist((self._x, self._y), (other._x, other._y))))
    def isNearby(self, p1):
        if self.distance(p1) < 5:
            return True
        return False
    def __str__(self):
        return "(" + str(self._x) + ", " + str(self._y) + ")"

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
p1 = Point(x1, y1)
p2 = Point(x2, y2)
print("The distance between the two points is", p1.distance(p2))
if (p1.isNearby(p2)): print("The two points are near to other")
else: print("The two points are not near to other")