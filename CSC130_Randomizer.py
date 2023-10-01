import random
names = ["Ellie", "Adaline", "Sebass", "Aiden", "Edin", "Riley", "Chloe", "Malachi", "Charloette", "Connor", "Ki", "Emily", "Christian", "Hannia", "Zach", "Alyssa", "Obasola", "Juan", "Emma", "Gianna", "Andrew", "Joanna", "Sarah", "Ashton", "Gabriela", "Alina", "Thomas", "Lantz", "Tucker", "Sammy", "David", "Chris", "Gabriel", "Braxton"]
print("Name Selection for Exam Practice:\n")
print('\033[1m' + names[0], '\033[0m' + "is paired with", '\033[1m' + names[1] + '\033[0m')
print('\033[1m' + names[2], '\033[0m' + "is paired with", '\033[1m' + names[3] + '\033[0m')
names.pop(0); names.pop(0); names.pop(0); names.pop(0)
while len(names) > 0:
    random.shuffle(names)
    print('\033[1m' + names[-1], '\033[0m' + "is paired with", '\033[1m' + names[-2] + '\033[0m')
    names.pop()
    names.pop()