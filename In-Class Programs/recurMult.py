# Multiplication
# Write a recursive function to calculate multiplication

def mult(n1, n2):
    if n1==0 or n2==0:
        return 0
    return n1+mult(n1, n2-1)
for i in range(3):
    n1, n2 = map(int, input().split())
    print(mult(n1, n2))