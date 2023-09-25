# Program #2:
def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):
    return investmentAmount*(1+monthlyInterestRate)**(12*years)

init = float(input("The amount invested: "))
interest = float(input("Annual interest rate: "))
print("Years Future Value")
for i in range (1, 31):
    print(i, futureInvestmentValue(init, interest/1200, i))