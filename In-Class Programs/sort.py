import random
def isSorted(lst):
    for k in range(1, len(lst)):
        if lst[k-1] > lst[k]:
            return False
    return True

lets = [chr(random.randint(65, 91)) for i in range(65, 91)]   # Random uppercase letter
print(lets)
if isSorted(lets):
    print("Sorted")
else:
    print("Not sorted")
