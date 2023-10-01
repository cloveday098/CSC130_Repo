# CSC130 Exam 1 Practice Questions

# Program #1: Soccer Ball
import math
v = float(input("Give a volume for your soccer ball: "))
a = round((4*v/(125+43*math.sqrt(5)))**(1/3), 2)
print("Side lengths are", "{:.2f}".format(a))   # Round but use format to make results ending with 0 to 2 digits

# Program #2: Car Depreciation
initVal = 42000
dep = 0.15
for i in range(1, 6):
    fv = str("{:.2f}".format(initVal*(1-dep)**(i)))
    fv = fv[0:2] + "," + fv[2:]
    print(str(i) + "\t" + "$" + fv)

# Program #3: Schedule Availability
days = "Sunday Monday Tuesday Wednesday Thursday Friday Saturday".split()
time = "morning afternoon evening".split()
studyHrs = 0
for i in range(7):
    for j in range(len(time)):
        s = int(input("How many hours did you study on " + days[i] + " " + time[j] + ": "))
        studyHrs += s
print("You studied", studyHrs, "hours this week.")

# Program 4: Double-Vowels
word = input("Enter a word, quit to stop: ").lower()
count, dv = 0, 0
while word != "quit":
    count += 1
    for i in range(len(word)-1):
        if word[i] in "aeiou" and word[i] == word[i+1]:
            dv += 1
            break
    word = input("Enter a word, quit to stop: ").lower()
print("Number of double vowel words entered:", dv)
print("Percentage of words entered that have double vowels:", str(round(100*dv/count, 2)) + "%")