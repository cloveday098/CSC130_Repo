# Project #5
x = float(input("Enter the x-coordinate of the point: "))
y = float(input("Enter the y-coordinate of the point: "))
if -5 <= x <= 5 and -2.5 <= y <= 2.5:
    print("Point", "(" + str(x) + ", " + str(y) + ") is in the rectangle")
else:
    print("Point", "(" + str(x) + ", " + str(y) + ") is not in the rectangle")