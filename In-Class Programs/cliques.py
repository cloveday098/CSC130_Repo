class Clique:
    def __init__(self, people, blackmail):
        self.people = people
        self._blackmail = blackmail
    def addPerson(self, p):
        self.people.append(p)
    def kickOut(self, p):
        self.people.remove(p)
    def __str__(self):
        s = ''
        for p in self.people:
            s += " " + p
        return s
    def printClique(self):
        print(self.people)

def main():
    cliq1 = Clique(["Chance", "Jorge"], "")
    cliq1.addPerson("Samir")
    cliq1.addPerson("Samir")
    cliq1.kickOut("Samir")
    cliq1.printClique()

main()