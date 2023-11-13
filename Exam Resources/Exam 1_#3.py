# Program #3: Pyramid of numbers
# This one is tricky

n = int(input("Enter a value for n: "))
# You want to loop n-1 line (half for the ascending pyramind and half for the descending pyramid)
for i in range(1, 2*(n)):
    # The first if handles the first half of the pyramid
    if i < n+1:
        for j in range(1, i+1):
            print(j, end=" ")   # Separate your numbers on a line with a space
    # You want to start descending (decreasing lines) after you reach the nth line
    else:
        for k in range(1, 2*n-i+1):
            print(k, end=" ")
    print()   # End a line with a newline