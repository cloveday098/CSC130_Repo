# CSC130 Exam 2 Practice Questions

# Program #1: Lunchbox
# Input is hard-coded because no mention of user input
class FoodItem:
    def __init__(self, foodName, gramsFat, gramsCarbs, gramsProtein):
        self.foodName = foodName
        self.gramsFat = gramsFat
        self.gramsCarbs = gramsCarbs
        self.gramsProtein = gramsProtein
        self.calories = float("{:.2f}".format(9*self.gramsFat + 4*self.gramsProtein + 4*self.gramsCarbs))
    def __lt__(self, other):
        return self.calories < other.calories
    def __str__(self):
        return self.foodName + " " + str(self.calories)

def main1():
    cheese = FoodItem("cheese",5,3,2)
    ham = FoodItem("ham",4,22,3)
    mayo = FoodItem("mayo",12,0,0)
    bread = FoodItem("bread",2.6,6.2,28)
    apple = FoodItem("apple",0,1,25)
    coke = FoodItem("coke",0.1,0.3,35.2)
    lunch = [cheese, ham, mayo, bread, apple, coke]
    correctOrd = 0
    i = 0
    try:
        while correctOrd != len(lunch) and i<len(lunch)-1:
            if not lunch[i].__lt__(lunch[i+1]):
                lunch[i], lunch[i+1] = lunch[i+1], lunch[i]
                i=0; correctOrd=0
            else:
                correctOrd+=1; i+=1
        raise Exception("oof")
    except:
        lunch.sort(key=lambda x:x.calories)

    for item in lunch: print(item)

# Program #2: String Sort
def upperCount(x):
    count = 0
    for i in x:
        if 'A' <= i <= 'Z':
            count += 1
    return count
def main2():
    try:
        infile = open("strings.txt", 'r')
        s = infile.read().split("\n")
        s.sort(key=lambda x:upperCount(x))
        for st in s: print(st)
        infile.close()
    except FileNotFoundError:
        print("File not found*!*")
    except Exception as e:
        print(e)

# Program #3: Minesweeper
def CountMines(m, n, board):
    if board[m][n] == "*": return "*"

    # Checking each of the possible 8 neighbors
    numbombs = 0
    for neigh in range(8):
        if neigh == 0 and m > 0 and n > 0:
            if board[m-1][n-1] == "*": numbombs += 1
        if neigh == 1 and m > 0:
            if board[m-1][n] == "*": numbombs += 1
        if neigh == 2 and m > 0 and n < len(board[m])-1:
            if board[m-1][n+1] == "*": numbombs += 1
        if neigh == 3 and n > 0:
            if board[m][n-1] == "*": numbombs += 1
        if neigh == 4 and n < len(board[m])-1:
            if board[m][n+1] == "*": numbombs += 1
        if neigh == 5 and m < len(board)-1 and n > 0:
            if board[m+1][n-1] == "*": numbombs += 1
        if neigh == 6 and m < len(board)-1:
            if board[m+1][n] == "*": numbombs += 1
        if neigh == 7 and m < len(board)-1 and n < len(board[m])-1:
            if board[m+1][n+1] == "*": numbombs += 1
    return numbombs

def main3():
    try:
        board = []
        row = list(input().rstrip())
        n = len(row)
        board.append(row)
        for i in range(n-1):
            row = list(input().rstrip())
            board.append(row)
        print(board)
        dims = (len(board[0]), len(board))
        adjboard = [[CountMines(__, _, board) for _ in range(dims[0])] for __ in range(dims[1])]
        for r in adjboard:
            for c in r:
                print(c, end="")
            print()
    except Exception as e:
        print(e)

# Program #4: Court Justices
def main4():
    try:
        infile = open("../In-Class Programs/inputfiles/Justices.txt")
        s = infile.read().split("\n")
        for judge in s:
            judge= judge.split(',')
            if len(judge) < 6: continue
            print(judge[0], judge[1], end=" ")
            if int(judge[-1]) == 0: print("is still serving")
            else: print("has served for", int(judge[-1]) - int(judge[-2]), "years")
        infile.close()
    except Exception as e:
        print("Go stuff yourself inside a vase and eaten by Upper Moon Four")

#main1()
#main2()
#main3()
#main4()