# Project #4:
import math
n = input("Enter numbers: ").split()
n = [float(num) for num in n]
mean = sum(n)/len(n)
print("The mean is", "{:.2f}".format(mean))
omega = 0
for i in n:
    omega += (i-mean)**2
omega = math.sqrt(omega/(len(n)-1))
print("The standard deviation is", omega)