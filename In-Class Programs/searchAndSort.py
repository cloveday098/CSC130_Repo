# Use linear and binary searches in practice ?'s
def linearSearch(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return -1

def binSearch(lst, key):
    low = 0
    high = len(lst) - 1
    while high >= low:
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return mid
        else:
            low = mid + 1
    return -low - 1  # Now high < low

#print(linearSearch([x for x in range(4, 9)], 8))
#print(binSearch([x for x in range(4, 9)], 8))



# Programs for Fri. 10/13:
# 1) Puzzler: Find a needle in a haystack (1/1 mil chance)
# The needle is represented by a 1 in a list of 0's
import random
haystack = [0 for h in range(1000000)]
haystack[random.randint(0,1000000)] = 1

print(linearSearch(haystack, 1))   # One approach
print(haystack.index(1))           # Another equally less-efficient approach
haystack.sort()                    # Then needle is haystack[-1]; could find original index by altering haystack to a list of tuples
print()


#2) Determine if a list is sorted
lets = [chr(i) for i in range(65,91)]
print(lets)

# Solution 1
sorted_nums = lets
sorted_nums.sort()
if lets == sorted_nums:
    print("Sorted")
else:
    print("Not sorted", "Should be", sorted_nums)

# Solution 2
def isSorted(lst):
    for k in range(1, len(lst)):
        if lst[k-1] > lst[k]:   # Not in order
            return False
    return True
if isSorted(lets):
    print("Sorted")
else:
    print("Not sorted")
print()


# 3) Lambda Sort
def lastLetter(s):
    if s == '':
        return ' '
    return s[-1]

a = ["apple", "banana", "pear", "peach", "pineapple", "zucchini", "plum"]
print(a)
a.sort(key=lambda x: len(x))
print(a)
a.sort(key=lambda x: lastLetter(x))   # Show that the function can be replaced with x[-1] but it is good notation to write functions for understanding purposes
print(a)
# Write another lambda sort and function in-class