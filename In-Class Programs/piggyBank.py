class PiggyBank:
    def __init__(self, q=0, d=0, n=0, p=0):
        self.__quarters = q
        self.__dimes = d
        self.__nickles = n
        self.__pennies = p
        self.__broken = False

    def breakBank(self):
        self.__quarters = self.__dimes = self__nickles = self.__pennies = 0
        self.__broken = True

    def repair(self):
        self.__broken = False

    def addQ(self, n):
        if self.__broken:
            return

        if n < 0:
            return

        self.__quarters += n
        pass

    def addD(self, n):
        if self.__broken:
            return

        if n < 0:
            return

        self.__dimes += n
        pass

    def addN(self, n):
        if self.__broken:
            return

        if n < 0:
            return

        self.__nickles += n
        pass

    def addP(self, n):
        if self.__broken:
            return

        if n < 0:
            return

        self.__pennies += n
        pass

    def totalValue(self):
        if self.__broken:
            return "Piggy bank is broken"

        total = self.__quarters * 25 + self.__dimes * 10 + self.__nickles * 5 + self.__pennies
        dollars = total // 100
        cents = total % 100

        return f"${dollars}.{cents:02d}"

    def __str__(self):
        return self.totalValue()

    def __lt__(self, other):
        return self.totalValue() < other.totalValue()

def main():
    p1 = PiggyBank(36, 28, 39, 5)
    voidbank = [p1, PiggyBank(10000000)]
    voidbank.sort()
    print(p1)
    print(voidbank[0].__lt__(voidbank[1]))

main()