def containsNeg(m):
    for row in m:
        lo = min(row)
        if lo < 0:
            return True
    return False

def isSparse(m):
    spots = 0
    ones = 0
    for row in m:
        spots += len(row)
        ones += row.count(1)
    if (ones/spots) > .5:
        return False
    return True

def print2d(twod):
    for i in range(len(twod)):
        for j in range(len(twod[i])):
            print(twod[i][j], end=" ")
        print()

def main():
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[0, 0, 1], [1, 0, 0], [0, 1, 1]]
    c = [[1, 2, 3], [-1, 0, 7], [0, 0, 0]]
    print2d(a)
    print(isSparse(b))
    print(containsNeg(c))
main()