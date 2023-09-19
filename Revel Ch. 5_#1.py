# Project #1

num = int(input("Enter an integer, the input ends if it is 0: "))
if num == 0: print("No numbers are entered except 0")
else:
    avg, count, pos, neg = 0, 0, 0, 0
    while num != 0:
        count += 1
        avg += num
        if num > 0: pos += 1
        elif num < 0: neg += 1
        num = int(input("Enter an integer, the input ends if it is 0: "))
    print("The number of positives is", pos)
    print("The number of negatives is", neg)
    print("The total is", avg)
    avg /= count
    print("The average is", avg)