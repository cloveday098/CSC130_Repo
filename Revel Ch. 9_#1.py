# Project #1:

class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def getArea(self):
        return self.w * self.h
    def getPerimeter(self):
        return 2*self.w + 2*self.h
    def printProperties(self):
        print(self.w, self.h, self.getArea(), self.getPerimeter())

rec1 = Rectangle(4, 40)
rec2 = Rectangle(3.5, 35.7)
rec1.printProperties()
rec2.printProperties()