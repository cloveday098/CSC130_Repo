# Project #1:
def grade(s, best):
    if s >= best-10:
        return "A"
    elif s >= best-20:
        return "B"
    elif s >= best-30:
        return "C"
    elif s >= best-40:
        return "D"
    else:
        return "F"

scores = input("Enter scores: ").split()
scores = [int(s) for s in scores]
for i in range(len(scores)):
    print("Student", i, "score is", scores[i], "and grade is", grade(int(scores[i]), int(max(scores))))