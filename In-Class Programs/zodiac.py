# Chinese Zodiac

year = int(input())
if year%12 == 0:
    sign = "Monkey"
elif year%12 == 1:
    sign = "Rooster"
elif year%12 == 2:
    sign = "Dog"
elif year%12 == 3:
    sign = "Pig"
elif year%12 == 4:
    sign = "Rat"
elif year%12 == 5:
    sign = "Ox"
elif year%12 == 6:
    sign = "Tiger"
elif year%12 == 7:
    sign = "Rabbit"
elif year%12 == 8:
    sign = "Dragon"
elif year%12 == 9:
    sign = "Snake"
elif year%12 == 10:
    sign = "Horse"
else:
    sign = "Sheep"
print("Your sign is", sign)