# Project #2

studs = int(input("Enter the number of students: "))
topName, secondName = "", ""
hiscore, secondHi = 0, 0
for i in range(studs):
    name = input("Enter a student name: ")
    score = float(input("Enter a student score: "))
    if score > secondHi:
        if score > hiscore:
            secondHi = hiscore
            secondName = topName
            hiscore = score
            topName = name
        else:
            secondHi = score
            secondName = name
print("Top two students:")
print(str(topName) + "'s score is", hiscore)
print(str(secondName) + "'s score is", secondHi)