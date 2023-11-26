# Program #2:

def gcd(m,n):
    if (m%n == 0): return n
    return gcd(n, m%n)
m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))
print("The GCD of", m, "and", n, "is", gcd(m,n))