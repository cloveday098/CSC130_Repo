# Project #2
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = float(input("Enter d: "))
e = float(input("Enter a: "))
f = float(input("Enter f: "))
if a*d-b*c == 0:
    print("The equation has no solution")
else:
    x = (e*d - b*f)/(a*d - b*c)
    y = (a*f - e*c)/(a*d - b*c)
    print("x is", x, "and y is", y)