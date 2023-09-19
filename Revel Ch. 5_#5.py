# Program #5

isbn = input("Enter the first 12 digits of an ISBN-13 as a string: ")
if (len(isbn) != 12):
    print("Incorrect input. It must have exact 12 digits")
else:
    checksum = 10 - (int(isbn[0]) + 3*int(isbn[1]) + int(isbn[2]) + 3*int(isbn[3]) + int(isbn[4]) + 3*int(isbn[5]) + int(isbn[6]) + 3*int(isbn[7]) + int(isbn[8]) + 3*int(isbn[9]) + int(isbn[10]) + 3*int(isbn[11])) % 10
    if checksum == 10: checksum = 0
    print("The ISBN-13 number is", isbn + str(checksum))