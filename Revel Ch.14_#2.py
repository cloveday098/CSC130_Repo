# Program #2:

words = list(set(input("Enter a text: ").split()))
words.sort()
for w in words: print(w, end=" ")