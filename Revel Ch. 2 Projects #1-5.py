# Revel Ch. 2 Programming Projects

# Project #1
#sub = float(input("Enter the subtotal: "))
#grat = float(input("Enter the gratuity rate: "))/100
#print("The gratuity is", "{:.2f}".format(grat*sub), "and the total is", "{:.2f}".format(sub*(1+grat)))

# Project #2
#min = int(input("Enter the number of minutes: "))
# min -> hrs -> days -> yrs
#yrs = min // 60 // 24 // 365
#days = min // 60 // 24 % 365
#print(min, "minutes is approximately", yrs, "and", days, "days")

# Project #3
#num = input("Enter an integer: ")
#print("The reversal is")
#count = 0
#while  len(num) > count:
#    print(num[-1-count])
#    count += 1

# Project #4
#x1 = float(input("Enter the x-coordinate for point1: "))
#y1 = float(input("Enter the y-coordinate for point1: "))
#x2 = float(input("Enter the x-coordinate for point2: "))
#y2 = float(input("Enter the y-coordinate for point2: "))
#dydx = (y2-y1)/(x2-x1)
#print("The slope for the line that connects two points (" + str(x1) + ",", str(y1) + ")", "and (" + str(x2) + ",", str(y2) + ")", "is", dydx)

# Project #5
#amt = float(input("Enter investment amount: "))
#interest = float(input("Enter annual interest rate: "))/1200
#yrs = int(input("Enter number of years: "))
#fia = amt * (1+interest)**(yrs*12)
#print("Accumulated value is", fia)

investmentAmount = float(input("Enter investment amount: "))
annualRate = float(input("Enter annual interest rate: "))
years = int(input("Enter number of years: "))
monthlyInterestRate = annualRate/1200
print(monthlyInterestRate)
futureInvestmentAmount = investmentAmount*(1+monthlyInterestRate)**(years*12)
print("Accumulated value is", futureInvestmentAmount)