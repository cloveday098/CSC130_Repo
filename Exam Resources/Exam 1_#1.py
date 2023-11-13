# Program #1: Prints uppercase letter count

s = input("Enter a string: ")
# You need to find how many capitalized letters are in s

count = 0   # Used to count how many uppercase letters you have
for i in s:   # You need to iterate through the entire string
    if i in "abcdefghijklmnopqrstuvwxyz".upper():   # If the current letter is capital it will be in that alphabet string.
        count += 1
    # OR you could specify the numerical range that a capital letter's ASCII value must be between ('A'-'Z')
    #if 65 <= ord(i) <= 90:
    #    count += 1
print(count)