# 1) Rose Bowl Scores [Pickle, Dicts, and Tuples]

def main1():
    import pickle
    rose = open("../In-Class Programs/inputfiles/RoseBowl.dat", 'rb')
    s = pickle.load(rose)
    for i in s.keys():
        if s[i][0][1] == s[i][1][1]:
            print("In", i, s[i][0][0], "tied with", s[i][1][0], "with a score of", s[i][0][1])
        elif max(s[i][0][1], s[i][1][1]) >= 48:
            print("In", i, end=" ")
            if s[i][0][1] > s[i][1][1]: print(s[i][0][0], "beat", s[i][1][0], "with a score of", s[i][0][1])
            else: print(s[i][1][0], "beat", s[i][0][0], "with a score of", s[i][1][1])
    rose.close()

# 2) Sum of Primes [Recursion]
def isPrime(n):
    if n == 1: return False
    for i in range(2,n-1):
        if n%i == 0: return False
    return True

def sumPrimes(n):
    if len(n) == 0:
        return 0
    if isPrime(n[0]):
        return n[0] + sumPrimes(n[1:])
    return sumPrimes(n[1:])

def main2():
    nums = [int(i) for i in input().split()]
    print(sumPrimes(nums))
    #print(sumEvens ([]))
    #print(sumEvens ([3,5,7,11]))
    #print(sumEvens ([1,3,4,9,13,23]))


# 3) Fibonacci Numbers [Recursion]
def fib(n):
    if n==0 or n==1: return n
    return fib(n-1) + fib(n-2)
def main3():
    for f in range(20): print(fib(f), end=" ")

# 4) Pairing Socks [Lists]
def main4():
    n = int(input())
    a = []
    line = input()
    values = list(map(int, line.split()))

    for q in values:
        if len(a) == 0 or a[-1] != q: a.append(q)
        else: a.pop()
    print(str(2*n) if len(a) == 0 else "impossible")

#5 Shape Matrix [Multi-D Lists]
def numOfUniqueSymbs(mat, nm):
    for m in range(len(mat)):
        row = set()
        if m==0:
            for _ in range(len(mat)):
                if mat[_][_] not in row: row.add(mat[_][_])
        elif m==3:
            for __ in range(len(mat)-1, 0, -1):
                if mat[__][__] not in row: row.add(mat[__][__])
        for n in range(len(mat)):
            if mat[m][n] not in row: row.add(mat[m][n])
        nm.append(len(row))
    return nm

def main5():
    matrix = []
    row = list(input().split())
    n = len(row)
    matrix.append(row)
    for i in range(n - 1):
        row = list(input().split())
        matrix.append(row)

    numMatrix = []
    numMatrix = numOfUniqueSymbs(matrix, numMatrix)
    for row in numMatrix: print(row)

# 6) Computer Pioneers [Files, dicts, & sets]

def main6():
    infile = open("../In-Class Programs/inputfiles/Pioneers.txt", 'r')
    s = infile.read().split("\n")
    s.remove('')
    feats = {}
    for p in s:
        p = p.split(',')
        if p[1] not in feats: feats[p[1]] = {p[0]}
        else: feats[p[1]].add(p[0])
    for item in feats.keys():
        if len(feats[item]) ==1:
            for person in feats[item]: print(person, end=" ")
        else: print(feats[item], end=" ")
        print(item)
    infile.close()

# 7) Coin Class [Classes, Inheritance]
def main7():
    class Coin():
        def __init__(self, count, worth):
            self.count = count
            self.worth = worth

        def value(self):
            return float("{:.2f}".format(self.count * self.worth))

    class Quarter(Coin):
        def __init__(self, count):
            super().__init__(count, .25)

    class Dime(Coin):
        def __init__(self, count):
            super().__init__(count, .1)

    class Nickel(Coin):
        def __init__(self, count):
            super().__init__(count, .05)

    class Penny(Coin):
        def __init__(self, count):
            super().__init__(count, .01)
    coins = []
    coins.append(Quarter(5).value())
    coins.append(Penny(2).value())
    coins.append(Nickel(3).value())
    coins.append(Dime(4).value())
    total = 0
    for c in coins:
        total += c
    print('$' + "{:.2f}".format(total))

# 8) Combinations
def fact(x):
    if x <= 2: return x
    return x*fact(x-1)

def main8():
    n, k = map(int, input("Values for n and k: ").split())
    while n <= 0 or k <= 0: n, k = map(int, input("Values for n and k: ").split())
    comb = fact(n)/(fact(n-k)*fact(k))
    print("A group of", n, "items given in groups of", k, "has", int(comb), "different combinations")

