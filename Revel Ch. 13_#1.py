# Program #1:

myfile = input("Enter a filename: ")
infile = open(myfile, 'r')
s = infile.read().split()
scores = 0
for x in s:
    scores += float(x)
print("There are", len(s), "scores")
print("The total is", int(scores))
print("The average is", scores/len(s))
infile.close()