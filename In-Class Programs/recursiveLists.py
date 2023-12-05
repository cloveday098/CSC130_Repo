# 1) Define a list of 10 random numbers and
# a) find the max using recursion and
# b) find the min using recursion

def findMax(n):
    # Base Cases: len 0 & 1
    if len(n) == 0: return
    elif len(n) == 1: return n[0]

    # Recursvive Compare
    else:
        mid = len(n)//2
        lHalf = n[:mid]
        rhalf = n[mid:]
        maxl = findMax(lHalf)
        maxr = findMax(rhalf)
        if maxl >= maxr:
            return maxl
        else:
            return maxr
        #return max(first, findMax(n))

import random
numlst = [random.randint(1,50) for i in range(10)]
print(numlst)
print(findMax(numlst))