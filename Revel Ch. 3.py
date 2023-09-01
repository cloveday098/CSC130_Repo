# Project #1
import math
#a = float(input("Enter your a-value here: "))
#b = float(input("Enter your b-value here: "))
#c = float(input("Enter your c-value here: "))
#discriminant = b*b - 4*a*c

#if (discriminant > 0):
#    r1 = (-b + math.sqrt(discriminant)) / (2 * a)
#    r2 = (-b - math.sqrt(discriminant)) / (2 * a)
#    print("The roots are ", r1, "and", r2)
#elif (discriminant == 0):
#    r1 = (-b + math.sqrt(discriminant)) / (2 * a)
#    print("The root is ", r1)
#else:
#    print("The equation has no real roots")

# Project #2
#a = float(input("Enter a: "))
#b = float(input("Enter b: "))
#c = float(input("Enter c: "))
#d = float(input("Enter d: "))
#e = float(input("Enter a: "))
#f = float(input("Enter f: "))
#if a*d-b*c == 0:
#    print("The equation has no solution")
#else:
#    x = (e*d - b*f)/(a*d - b*c)
#    y = (a*f - e*c)/(a*d - b*c)
#    print("x is", x, "and y is", y)

# Project #3
m = int(input("Enter a month in the year (e.g., 1 for Jan): "))
yr = int(input("Enter a year: "))
if m==1:
    month = "January"
    days = 31
elif m==2:
    month = "February"
    if yr%4 == 0:
        days = 29
    else:
        days = 28
elif m==3:
    month = "March"
    days = 31
elif m==4:
    month = "April"
    days = 30
elif m==5:
    month = "May"
    days = 31
elif m==6:
    month = "June"
    days = 30
elif m==7:
    month = "July"
    days = 31
elif m==8:
    month = "August"
    days = 31
elif m==9:
    month = "September"
    days = 30
elif m==10:
    month = "October"
    days = 31
elif m==11:
    month = "November"
    days = 30
else:
    month = "December"
    days = 31
print(month, yr, "has", days, "days")

# Project #4

# Project #5
