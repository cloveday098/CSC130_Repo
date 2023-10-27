# Program #6
# Adjacency matrices bringing me back to Frogger in Algorithms

import math
def findCentral(m, cities):
    for i in range(len(m)):
        x1, y1 = float(cities[2*i]), float(cities[2*i + 1])
        for j in range(len(m)):
            x2, y2 = float(cities[2*j]), float(cities[2*j + 1])
            m[i][j] = math.dist((x1, y1), (x2, y2))
    minDist, cx, cy = sum(m[0]), cities[0], cities[1]
    print(m)
    for k in range(1, len(m)):
        if sum(m[k]) < minDist:
            minDist = sum(m[k])
            cx, cy = cities[2*k], cities[2*k+1]
    return (float(cx), float(cy))

cities = input("Enter the coordinates of the cities: " ).split()
adj = [[i for i in range(len(cities)//2)] for j in range(len(cities)//2)]
print("The central city is at", findCentral(adj, cities))