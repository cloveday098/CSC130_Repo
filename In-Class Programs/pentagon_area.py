import math

r = float(input("Radius: "))
s= 2*r*math.sin(math.pi/5)
a = (5*s*s)/(4*math.tan(math.pi/5))
print(s, a)