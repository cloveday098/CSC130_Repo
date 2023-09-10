# Project #2
let = input("Enter a letter grade: ")
begin = "The numeric value for grade"
if (let == 'A' or let == 'a'):
    print(begin, let, "is 4")
elif (let == 'B' or let == 'b'):
    print(begin, let, "is 3")
elif (let == 'C' or let == 'c'):
    print("The numeric value for grade", let, "is 2")
elif (let == 'D' or let == 'd'):
    print("The numeric value for grade", let, "is 1")
elif (let == 'F' or let == 'f'):
    print("The numeric value for grade", let, "is 0")
else:
    print(let, "is an invalid grade")