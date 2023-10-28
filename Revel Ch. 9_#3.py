# Project #3:

class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y
    def getx(self):
        return self._x
    def gety(self):
        return self._y
    def distance(self, other):
        return math.distance(self, other)
    def isNearby(self, p1):
        if self.distance(p1) < 5:
            return True
        return False
    def __str__(self):
        return "(" + str(self._x) + ", " + str(self._y) + ")"
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
p1 = Point(x1, y1)
p2 = Point(x2, y2)
print("The distance between the two points is", p1.distance(p2))
if (p1.isNearby(p2)): print("The two points are near to other")
else: print("The two points are not near to other")