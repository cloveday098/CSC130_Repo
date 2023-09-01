import math
x1, x2 = map(int, input().split())
y1, y2 = map(int, input().split())
dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(dist)