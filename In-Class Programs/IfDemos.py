n = int(input("Give me a number: "))
print("Divisible by 2 or 3:", (n%2==0 or n%3!=0))
print("Divisible by 2 and 3:", (n%2==0 and n%3!=0))
print("Divisible by 2 or 3 but not both:", (n%2==0 and n%3!=0) or (n%2!=0 and n%3==0))

print()
num = int(input("Give me a number: "))
if num%5 == 0:
    print("HiFive")
if num%2 ==0:
    print("HiEven")