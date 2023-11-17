# Program #2: Min Value of 2D Array

def GetMinVal(arr):
    minVal = arr[0][0]
    for i in arr:
        i.sort()
        if minVal > i[0]: minVal = i[0]
    return minVal

matrix = []
row = "hi"
while True:
    row = [int(n) for n in input().split()]
    if len(row) <= 0: break
    matrix.append(row)
print("The min value of this array is", GetMinVal(matrix))