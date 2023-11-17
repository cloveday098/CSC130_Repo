# Program #1: Sort by Consonants

def numofcons(w):
    cons = 0
    for letter in w:
        if letter.upper() not in ['A', 'E', 'I', 'O', 'U']: cons += 1
    return cons

infile = open("../In-Class Programs/inputfiles/Words.txt", 'r')
words = infile.read().split("\n")
words.remove('')
words.sort(key=numofcons)
infile.close()
for w in words: print(w)