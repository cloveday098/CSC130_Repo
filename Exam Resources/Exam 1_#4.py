# Program #4: Palindrome

word = input()
i, j = 0, len(word)-1
isPal = True

# i starts at the front, j at the back; if they pass each other, stop searching
while i <= j:
    if word[i] != word[j]:
        print("not palindrome")
        isPal = False
        break
    i += 1
    j -= 1
if isPal:
    print("palindrome")