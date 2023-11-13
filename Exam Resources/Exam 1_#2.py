# Program #2: Calculate height

import math
# Take in your four inputs
V = float(input("Enter V: "))
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# Rearrange the formula to solve for h
h = 4*V/ math.sqrt(-a**4 + 2*(a*b)**2 + 2*(a*c)**2 - b**4 +2*(b*c)**2 - c**4)
print("h =", "{:.2f}".format(h))