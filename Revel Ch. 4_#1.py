# Project #1
import math
n = int(input("Enter the number of sides: "))
s = float(input("Enter the length of a side: "))
a = (n*s**2) / (4*math.tan(math.pi/n))
print("The area of the polygon is", a)