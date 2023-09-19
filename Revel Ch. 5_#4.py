# Program #4

s = input("Enter a string: ")
v = s.count("A") + s.count("a") + s.count("E") + s.count("e") + s.count("I") + s.count("i") + s.count("O") + s.count("o") + s.count("U") + s.count("u")
c = 0
for i in range(len(s.strip())):
    if s[i] not in ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"] and s[i].isalpha():
        c += 1
print("The number of vowels is", v)
print("The number of consonants is", c)