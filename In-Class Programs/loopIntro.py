age = int(input("Gimme your age: "))
while age < 0 or age > 150:
    age = int(input("A realistic age, please: "))
if age < 18:
    print("child")
elif age < 65:
    print("adult")
elif age > 110:
    print("You're dead (at least to reality)!")
else:
    print("senior")