c1 = input("Enter City1: ")
c2 = input("Enter City2: ")
c3 = input("Enter City3: ")

if c1 <= c2 <= c3:
    print(c1, c2, c3)
elif c2 <= c1 <= c3:
    print(c2, c1, c3)
elif c1 <= c3 <= c2:
    print(c1, c3, c2)
elif c2 <= c3 <= c1:
    print(c2, c3, c1)
elif c3 <= c1 <= c2:
    print(c3, c1, c2)
else:
    print(c3, c2, c1)