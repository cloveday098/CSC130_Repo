# Project #1
import math
a = float(input("Enter your a-value here: "))
b = float(input("Enter your b-value here: "))
c = float(input("Enter your c-value here: "))
discriminant = b*b - 4*a*c

if (discriminant > 0):
    r1 = (-b + math.sqrt(discriminant)) / (2 * a)
    r2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("The roots are ", r1, "and", r2)
elif (discriminant == 0):
    r1 = (-b + math.sqrt(discriminant)) / (2 * a)
    print("The root is ", r1)
else:
    print("The equation has no real roots")
