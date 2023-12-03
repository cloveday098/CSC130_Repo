# Palindrome Checker
def palindromeHelper(word, start, end):
    if start == end or start >= end:
        return True
    elif word[start] != word[end]:
        return False
    else:
        return palindromeHelper(word, start+1, end-1)

def isPalindrome(word):
    return palindromeHelper(word, 0, len(word)-1)

print(isPalindrome("tacocat"))
print(isPalindrome("no"))