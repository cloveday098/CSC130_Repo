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