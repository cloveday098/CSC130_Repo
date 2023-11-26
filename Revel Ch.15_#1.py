# Program #1:

def sumDigits(n):
    if 0<=n<=9: return n
    return int(str(n)[0]) + sumDigits(int(str(n)[1:]))
num = int(input("Enter an integer: "))
print("The sum of digits in", num, "is", sumDigits(num))