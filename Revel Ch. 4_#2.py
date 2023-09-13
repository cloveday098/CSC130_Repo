# Project #2
letgrade = input("Enter a letter grade: ")
begin = "The numeric value for grade"
l, letgrade = letgrade, letgrade.upper()
match letgrade:
    case "A":
        print(begin, l, "is 4")
    case "B":
        print(begin, l, "is 3")
    case "C":
        print(begin, l, "is 2")
    case "D":
        print(begin, l, "is 1")
    case "F":
        print(begin, l, "is 0")
    case _:
        print(letgrade, "is an invalid grade")

if (letgrade == 'A' or letgrade == 'a'):
    print(begin, letgrade, "is 4")
elif (letgrade == 'B' or letgrade == 'b'):
    print(begin, letgrade, "is 3")
elif (letgrade == 'C' or letgrade == 'c'):
    print("The numeric value for grade", letgrade, "is 2")
elif (letgrade == 'D' or letgrade == 'd'):
    print("The numeric value for grade", letgrade, "is 1")
elif (letgrade == 'F' or letgrade == 'f'):
    print("The numeric value for grade", letgrade, "is 0")
elif letgrade.upper() > "F" or letgrade.upper() == "E":
# else:
    print(letgrade, "is an invalid grade")