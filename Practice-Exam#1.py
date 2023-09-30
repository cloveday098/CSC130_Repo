import math
v = float(input("Give a volume for your soccer ball: "))
a = round((4*v/(125+43*math.sqrt(5)))**(1/3), 2)
print("Side lengths are", "{:.2f}".format(a)) 