amt = float(input("How much in pennies: "))
dollars = amt//100
amt = amt % 100
qrts = amt//25
amt = amt % 25
dms = amt//10
amt = amt % 10
niks = amt//5
pens = amt % 5
print(dollars, "dollars", qrts, "quarters", dms, "dimes", niks, "nickels", pens, "pennies")