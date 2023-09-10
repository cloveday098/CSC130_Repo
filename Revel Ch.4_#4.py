# Project #4
first_nine = input("Enter the first 9 digits of an ISBN as a string: ")
if (len(first_nine) != 9):
    print("Incorrect input. It must have exact 9 digits")
else:
    checksum = (int(first_nine[0]) + int(first_nine[1])*2 + int(first_nine[2])*3 + int(first_nine[3])*4 + int(first_nine[4])*5 + int(first_nine[5])*6 + int(first_nine[6])*7 + int(first_nine[7])*8 + int(first_nine[8])*9) % 11
    if checksum == 10:
        end = 'X'
    else:
        end = str(checksum)
    print("The ISBN-10 number is", str(first_nine) + end)