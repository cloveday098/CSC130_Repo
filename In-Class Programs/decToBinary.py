# Decimal to Binary Convertor

def DecToBin(n):
    if n==1 or n==0: return n
    q = n//2
    r = n%2
    return str(r) + str(DecToBin(q))
print(DecToBin(8))