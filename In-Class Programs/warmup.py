# Divisible
n = int(input())
if (n % 2 == 0 or n % 3 ==0):
    print("or")
elif (n % 2 == 0 and n % 3 ==0):
    print("and")
elif (n % 2 ==0 and n % 3 != 0) or (n % 2 != 0 and n % 3 == 0):
    print("one but not both")

# Leapyear
yr = int(input("ENter a year: "))
leap = ((yr%4 ==0 and yr%100 != 0) or yr%400 == 0)
print(leap)