import random
lotNum = random.randint(0,99)
guess = input("Pick a number from 0-99: ")
while(True):
    try:
        val = int(guess)
    except ValueError:
        print('Valid number, please')
        continue
    if (val < 0 or val > 99):
        print('Valid range, please: 0-99')
    else:
        break
    guess = input("Pick a number from 0-99: ")

print(lotNum, "You guessed", guess)
digit1 = lotNum % 10
digit2 = lotNum // 10
digit_a = val % 10
digit_b = val // 10
if (lotNum == guess):
    m = 10000
elif ((digit1 == digit_a or digit1 == digit_b) and (digit2) == digit_a or digit2 == digit_b):
    m = 3000
elif ((digit1 == digit_a) or (digit2 == digit_b)):
    m = 1000
else:
    m = 0
    print("You won a whoppin' $0")
if m > 0:
    print("You won", "$" + str(m))