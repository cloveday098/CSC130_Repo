# Program #3:
def wCount(w, c):
    return len(w) - len(w.replace(c, ''))

words = input("Enter a string: ")
c = input("Enter a character: ")
print(c, "appears in", words, wCount(words, c), "times")