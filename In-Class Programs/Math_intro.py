
print(chr(0x26c4))

# Angles of a triangle
import math
a = int(input())
b = int(input())
c = int(input())
A = math.degrees(math.acos((a*a - b*b - c*c)/(-2*b*c)))
B = math.degrees(math.acos((b*b - a*a - c*c)/(-2*a*c)))
C = math.degrees(math.acos((c*c - a*a - c*c)/(-2*a*b)))
print(A, B, C)