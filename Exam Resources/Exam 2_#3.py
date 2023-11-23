# Program #3: Justices Class

class SCJ:
    def __init__(self, last, first, pres, st, bd, ed):
        self.last = last
        self.first = first
        self.pres = pres
        self.st = st
        self.bd = int(bd)
        self.ed = int(ed)
    def __str__(self):
        return self.first + " " + self.last
    def __lt__(self, other):
        return self.ed-self.bd < other.ed-other.bd

def main():
    scjs = []
    try:
        infile = open("../In-Class Programs/inputfiles/Justices.txt", 'r')
        s = infile.read().split("\n")
        s.remove('')
        for i in s:
            judge = i.split(",")
            ed = int(judge[5])
            if int(judge[5]) == 0: ed = 2023
            scjs.append(SCJ(judge[1], judge[0], judge[2], judge[3], judge[4], ed))
            scjs.sort()
        infile.close()
    except Exception as e:
        print(e)
    try:
        outfile = open("justices2.txt", 'w')
        for j in scjs: outfile.writelines(str(j) + "\n")
        outfile.close()
    except Exception:
        print("Outfile error")
main()