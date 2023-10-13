def lastLetter(s):
    if s == "":
        return " "
    return s[-1]

a = ["apple", "banana", "pear", "peach", "dragonfruit", "plum", "durian"]
print(a)
a.sort(key= lambda c: lastLetter(c))
print(a)