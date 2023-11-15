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


# 2) Work Hours Table
def main2():
    infile = open("workhrs.txt", 'r')
    s = infile.read().split("\n")
    weeklyHours = [[x for x in y.split()] for y in s]

    print("\t\t\t\tWeekly Payroll")
    print("Employee\t\t Hours\t\t\t Pay")
    print("_________\t\t _____\t\t   _______")
    for i in range(len(weeklyHours)):
        print(weeklyHours[i][0], end="\t\t  ")
        totalhrs = 0
        totalPay = 0.0
        for j in range(1, len(weeklyHours[i])):
            totalhrs += int(weeklyHours[i][j])
            if j==1 or j==7:
                totalPay += 15 * 1.5 * int(weeklyHours[i][j])
            else:
                totalPay += 15 * int(weeklyHours[i][j])
        print(totalhrs, end="\t\t   ")
        print('$'+str("{:.2f}".format(totalPay)))
        infile.close()


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


# 4) Exchange Rates
def main4():
    infile = open("../In-Class Programs/inputfiles/Exchrate.txt", 'r')
    s = infile.read().split("\n")
    s.remove("")
    rates = [d.split(",") for d in s]
    infile.close()
    outfile = open("rates.txt", 'w')
    for country in rates:
        print(country)
        outfile.write("The " + str(country[1]) + " in " + country[0] + " is " + str(country[2]) + " times the value of the American dollar\n")
    outfile.close()


# 5) Spotify Playlist Class
class playlist:
    def __init__(self, name, creator, length, genre):
        self.__name = name
        self.__creator = creator
        self.__playtime = length
        self.__genre = genre
    def __lt__(self, other):
        return self.__playtime < other.__playtime
    def __str__(self):
        return str(self.__name) + " (" + str(self.__creator) + "): " + str(self.__playtime) + " hrs"

def main5():
    play1 = playlist("Vibe", "Chance", 2.417, "Instrumental & Pop")
    play2 = playlist("Drive, Power, and Inspiration", "Chance", 2.117, "Classic Rock & Hip Hop")
    play3 = playlist("Jorge's Playlist", "Jorge", 1.789, "Pop and Skillet")
    mixes = [play1, play2, play3]
    mixes.sort()
    for p in mixes: print(p)

#main1()
main2()
#main3()
#main4()
#main5()