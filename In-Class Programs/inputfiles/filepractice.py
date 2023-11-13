infile = open("Words.txt")
words = [x for x in infile.read().split()]

print(words)