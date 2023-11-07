# Program #2:

flnm = input("Enter a filename: ")
file = open(flnm, 'r')
words = file.read().split()
sWords = words.copy(); sWords.sort()
srt = True
for i in range(len(words)):
    if words[i] != sWords[i]:
        print("The words are not sorted. The first two out-of-order words:", words[i], words[i+1])
        srt = False
        break
if srt: print("The words are sorted.")
file.close()