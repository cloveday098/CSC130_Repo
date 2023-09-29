# CSC130 Exam 1 Practice Questions

# Program #1: Soccer Ball
import math
v = float(input("Give a volume for your soccer ball: "))
a = round((4*v/(125+43*math.sqrt(5)))**(1/3), 2)
print("Side lengths are", "{:.2f}".format(a))   # Round but use format to make results ending with 0 to 2 digits

# Program #2: Car Depreciation
initVal = 42000
dep = 0.15
for i in range(1, 6):
    print(str(i) + "\t" + str("{.2f}".format(initVal*(1+dep)**(i))))
