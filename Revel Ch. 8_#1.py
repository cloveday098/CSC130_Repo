# Program #1

def sumColumn(m, columnIndex):
    total = 0
    for row in m:
        total += row[columnIndex]
    print("Sum of the elements for column", columnIndex, "is", total)

mat = [[] for i in range(3)]
mat[0] = [float(val) for val in input("Enter a 3-by-4 matrix row 0: ").split()]
mat[1] = [float(val) for val in input("Enter a 3-by-4 matrix row 1: ").split()]
mat[2] = [float(val) for val in input("Enter a 3-by-4 matrix row 2: ").split()]
for c in range(4):
    sumColumn(mat, c)