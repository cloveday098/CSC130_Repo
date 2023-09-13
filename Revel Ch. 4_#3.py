# Project #3
yr = int(input("Enter a year: "))
m = input("Enter a month: ")
if m == "Jan" or m == "Mar" or m == "May" or m == "Jul" or m == "Aug" or m == "Oct" or m == "Dec":
    days = 31
elif m == "Apr" or m == "Jun" or m == "Sept" or m == "Nov":
    days = 30
elif m == "Feb":
    if yr%4==0: days = 29
    else: days = 28
else:
    days = 0
    print(m, "is not a correct month name")
if days != 0: print(m, yr, "has", days, "days")