# Program #3:

def reverseDisplay(val):
    vallst = [x for x in val]
    vallst.reverse()
    rev = ""
    for i in vallst: rev += i
    print(rev)
val = input("Enter a string: ")
reverseDisplay(val)