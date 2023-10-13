import random
nums = [54,22,15,48,332]
evens = [num for num in nums if num%2 == 0]
print(evens)

nums = [random.randint(0,99) for i in range(100)]
avg = sum(nums)/len(nums)
above = [n for n in nums if n > avg]
print(avg)
print(above)