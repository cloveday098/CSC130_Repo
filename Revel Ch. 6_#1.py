# Program #1:
print("i m(i)")
sum = 0
for i in range(1, 21):
    sum += i/(i+1)
    print(i, "{:.4f}".format(sum))