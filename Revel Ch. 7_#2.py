# Project #2:
nums = input("Enter integers between 1 and 100, inclusive: ").split()
nums = [int(s) for s in nums]
nums.sort()
countNums, score = [], []
for i in nums:
    if i not in countNums:
        print(i)
        countNums.append(i)
        score.append(1)
    else:
        score[-1] += 1
for j in range(len(countNums)):
    print(countNums[j], "occurs", score[j], "time", end="")
    if score[j] > 1: print("s")
    else: print()