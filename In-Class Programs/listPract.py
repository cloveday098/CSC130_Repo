def func(number, numbers):
    number = 1001
    numbers[0] = 5555

def main():
    x = 1
    y = [1, 2, 3]
    func(x, y)
    print(x)
    print(y)
main()

def combineLists(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        result.append((lst1[i], lst2[i]))
    return result
lst1 = [x for x in range(56, 98)]
lst2 = [True for j in range(56, 98)]

print(combineLists(lst1, lst2))