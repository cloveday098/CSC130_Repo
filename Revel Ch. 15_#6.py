# Program #6:

def binaryToDecimal(bs):
    if len(bs) == 1: return int(bs[0])
    return int(bs[0])*2**(len(bs)-1) + binaryToDecimal(bs[1:])
binNum = input("Enter a binary number: ")
print(binNum, "is decimal", binaryToDecimal(binNum))