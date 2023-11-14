# Additional Practice for CSC130 Exam 2

# 1) Write functions to calculate the median and standard deviation of a list of numbers.
import math
def median(n):
    if n == []: return None
    n.sort()
    if len(n)%2 == 1:
        return n[len(n)//2]
    else: return 0.5*(n[len(n)//2] + n[len(n)//2+1])

def mean(n):
    return sum(n)/len(n)

def stdev(n):
    if n == []: return None
    total = 0
    m = mean(n)
    for i in n:
        total += (i-m)*(i-m)
    total = math.sqrt(total/len(n))
    return total

def main1():
    numlst = [float(x) for x in input().split()]
    print("The median is", median(numlst))
    print("The standard deviation is", stdev(numlst))


# 2) Write a program to calculate the total calories of a lunch
def main2():
    class FoodItem:
        def __init__(self, foodName = '', gramsFat = 0.0, gramsCarbs = 0.0, gramsProtein = 0.0):
            self.foodName = foodName
            self.gramsFat = gramsFat
            self.gramsCarbs = gramsCarbs
            self.gramsProtein = gramsProtein
        def num_of_cals (self):
            return 9*self.gramsFat + 4*self.gramsCarbs + 4*self.gramsProtein
        def __str__(self):
            return self.foodName
    bread = FoodItem("bread", 2.6, 6.2, 28)
    cheese = FoodItem("cheese", 5.3, 2)
    turkey = FoodItem("turkey", 4, 0, 25)
    apple = FoodItem("apple", 0.1, 25)
    coke = FoodItem("coke", 0.1, 0.3, 35.2)

    lunch = [bread, cheese, turkey, apple, coke]
    totalCalories = 0.0
    for item in lunch:
        totalCalories += item.num_of_cals()
        print(item)
    print("The total number of calories in this lunch is", "{:.2f}".format(totalCalories), "calories.")


# 3) Sort all the colleges and universities in the Colleges.txt file, and print each out according to their respective states

def main3():
    infile = open("../In-Class Programs/inputfiles/Colleges.txt", 'r')
    s = infile.read().split("\n")
    s.remove('')
    colleges = [[x for x in s[i].split(",")] for i in range(len(s))]
    colleges.sort(key= lambda x:x[1])

    # Print Out by State
    states = []
    for i in colleges:
        if i[1] not in states:
            states.append(i[1])
            if i != colleges[0]: print()
            print(i[1] + ": ", end="")
        if i != colleges[-1]: print(i[0], end="\t")
        else: print(i[0])
    infile.close()

#main1()
#main2()
main3()