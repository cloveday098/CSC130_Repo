# Program #5:

def decimalToBinary(n):
    if n==1 or n==0: return n
    q = n//2
    rem = str(n%2)
    return str(decimalToBinary(q)) + rem
num = int(input("Enter a decimal integer: "))
print(num, "is binary", decimalToBinary(num))