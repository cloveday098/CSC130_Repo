# Program #1:

text = input("Enter a text: ").replace(" ", "")
vows = 0
for c in text:
    if c.upper() in {"A", "E", "I", "O", "U"}:
        vows += 1
print("The number of vowels is", vows, "and consonants is", len(text)-vows)