# Phone Dialog Box
word = input("What's the gate word? ").upper()
print("The code for", word, "is ", end="")
c1, c2, c3, c4 = word[0], word[1], word[2], word[3]
num1, num2, num3, num4 = ord(c1)-65, ord(c2)-65, ord(c3)-65, ord(c4)-65

for i in range(4):
    if num1//3 == 0:
        code1 = 2
    elif num1//3 == 1:
        code1 = 3
    elif num1//3 == 2:
        code1 = 4
    elif num1//3 == 3:
        code1 = 5
    elif num1//3 == 4:
        code1 = 6

    elif 15 <= num1 <= 18:
        code1 = 7
    elif 19 <= num1 <= 21:
        code1 = 8
    elif 22 <= num1 <= 25:
        code1 = 9
    else:
        print(i, num1)
        print("Nope")
    if (i==0): num1 = num2
    if (i==1): num1 = num3
    if (i==2): num1 = num4
    print(code1, end="")