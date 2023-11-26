# Program #4:

def countUppercaseHelper(s, high):
    return high + len([i for i in s if i.isupper()])

def countUppercase(s):
    high = 0
    if len(s) == 0: return high
    high += countUppercaseHelper(s[-1], high)
    s.pop()
    return high + countUppercase(s)

word = input("Enter a string: ")
print("The uppercase letters in", word, "is", countUppercase(word.split()))