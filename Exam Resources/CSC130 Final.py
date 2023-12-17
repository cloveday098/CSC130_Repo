# Time: 4:28 (about 58 minutes, including correcting #4)
#1 Superbowl Wins & Losses
def main1():
    import pickle
    infile = open("../In-Class Programs/inputfiles/Superbowl.dat", 'rb')
    teams = pickle.load(infile)
    infile.close()
    winners = set()
    losers = set()
    for team in teams.keys():
        winners.add(teams[team]['winner'])
        losers.add(teams[team]['opposition'])
    #print(winners.intersection(losers))
    print("These teams have both won and lost the Superbowl:")
    for t in winners.intersection(losers):
        print(t)

#2 Miami Superbowls
def main2():
    import pickle
    infile = open("../In-Class Programs/inputfiles/Superbowl.dat", 'rb')
    sb = pickle.load(infile)
    infile.close()
    for yr in sb.keys():
        if sb[yr]['venue'] == 'Miami':
            print(yr, "Winner:", sb[yr]['winner'], "  Other Team:", sb[yr]['opposition'], "  Score", sb[yr]['score'])

#3 Greatest Superbowl Point Difference
def main3():
    import pickle
    infile = open("../In-Class Programs/inputfiles/Superbowl.dat", 'rb')
    sb = pickle.load(infile)
    infile.close()

    scoreDiffs = set()
    for yr in sb.keys():
        s = sb[yr]['score'].split('-')
        diff = abs(int(s[0])-int(s[1]))
        scoreDiffs.add((diff, yr))

    top = max(scoreDiffs)
    print("The greastest score difference was", top[0])
    print("In", str(top[1]) + ',', sb[top[1]]['winner'], "beat", sb[top[1]]['opposition'], "with a score of", sb[top[1]]['score'], "at", sb[top[1]]['venue'])

#4: Derangements
def D(n):
    if n==1: return 0
    return n*D(n-1) + (-1)**n

def main4():
    for n in range(1,11):
        print(D(n))

#5 Even vs. Odd
def evenHelper(n, high):
    if len(n)==0: return high
    if n[-1]%2 == 0: return evenHelper(n[0:-1], high+1)
    return evenHelper(n[0:-1], high)

def moreEven(lst):
    evens = 0
    if len(lst) == 0: return False
    evens = evenHelper(lst, evens)
    if (evens > len(lst)-evens):
        return True
    return False

def main5():
    print(moreEven([]))
    print(moreEven([2]))
    print(moreEven([3]))
    print(moreEven([5, 6, 3, 4, 8, 10, 12, 7]))
    print(moreEven([5, 7, 3, 4, 8, 10, 12, 9, 11]))

main5()