import random

def linearSearch(lst, key):
    for j in range(len(lst)):
        if lst[j] == key:
            return j
    return False

haystack = [0 for i in range(1000000)]
haystack[random.randint(0, 1000000)] = 1 # Needle

print(linearSearch(haystack, 1))