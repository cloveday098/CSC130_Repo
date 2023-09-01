# Project #4
yr = int(input("Enter year: (e.g., 2008): "))
m = int(input("Enter month: 1-12: "))
if m == 1 or m == 2:
    m += 12
    yr -= 1
q = int(input("Enter the day of the month: 1-31: "))
j = yr//100
k = yr%100
h = (q + 26*(m+1)//10 + k + k//4 +j//4 +5*j) % 7
if h==0:
    day = "Saturday"
elif h==1:
    day = "Sunday"
elif h==2:
    day = "Monday"
elif h==3:
    day = "Tuesday"
elif h==4:
    day = "Wednesday"
elif h==5:
    day = "Thursday"
else:
    day = "Friday"
print("Day of the week is", day)