class Animal:
    def __init__(self, numLegs, sound):
        self.__legs = numLegs
        self.__sound = sound
    def __str__(self):
        return self.__sound
class Mammal(Animal):
    def __init__(self, hair, egglaying, numLegs=4, sound=""):
        super().__init__(numLegs, sound)
        self.__hair = hair
        self.__egglaying = egglaying

class Arachnid(Animal):
    def __init__(self, numLegs=0, sound=''):
        super().__init__()
class Spider(Arachnid):
    def __init__(self):
        super().__init__(8)
class Dog(Mammal):
    def __init__(self, tricks, name):
        super().__init__(True, False, 4, "woof")
        self.__tricks = tricks
        self.__name = name
    def __str__(self):
        return self.__name + " says " + super().__str__()
class Cat(Mammal):
    def __init__(self, name):
        super().__init__(True, False, 4, "meow")
        self.__name = name
    def __str__(self):
        return (super().__str__() + " ")*3

spot = Dog("Sit", "Spot")
will = Cat("Will")
print(spot)
print(will)