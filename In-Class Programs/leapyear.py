yr = int(input("Enter a year: "))
leap = ((yr%4 ==0 and yr%100 != 0) or yr%400==0)
print(leap)
