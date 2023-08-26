sub = float(input("Enter the subtotal: "))
grat = float(input("Enter the gratuity rate: "))/100
print("The gratuity is", "{:.2f}".format(grat*sub), "and the total is", "{:.2f}".format(sub*(1+grat)))