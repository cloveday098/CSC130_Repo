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
    fv = initVal*(1-dep)**(i)
    print(str(i) + "\t" + str("{:.2f}".format(fv)))

# Program #3: Schedule Availability
#days = "Sunday Monday Tuesday Wednesday Thursday Friday Saturday".split()
#time = "morning afternoon evening".split()
#studyHrs = 0
#for i in range(7):
#    for j in range(len(time)):
#        s = int(input("How many hours did you study on " + days[i] + " " + time[j] + ": "))
#        studyHrs += s
#print("You studied", studyHrs, "hours this week.")

# Program 4: RFL
gender = input("What is your gender: M/F? ")
height = float(input("What is your height in cm? "))
wm = float(input("What does your waist measure in cm? "))
if gender == "M":
    RFL = 64-(20*height/wm)
    if RFL <= 5:
        status = "low"
    elif RFL <= 13:
        status = "athletic"
    elif RFL <= 24:
        status = "average"
    else:
        status = "obese"
elif gender == "F":
    RFL = 76-(20*height/wm)
    if RFL <= 13:
        status = "low"
    elif RFL <= 20:
        status = "athletic"
    elif RFL <= 31:
        status = "average"
    else:
        status = "obese"
print("RFL:", str("{:.2f}".format(round(RFL, 2))) + "%:", "(" + status + ")")