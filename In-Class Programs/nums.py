infile = open("inputfiles/numbers.txt")
sum = 0
while True:
    s = infile.readline()
    if not s: break
    sum += eval(s)
print(sum)
infile.close()