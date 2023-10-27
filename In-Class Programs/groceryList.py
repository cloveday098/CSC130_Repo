def getGroceryItem():
    name = input("Name of item: ")
    if name == "":
        return None
    q = int(input("Quantity of item: "))
    p = float(input("Price of item: "))
    return (name, q, p)

def printReceipt(groc, sub, tax, total):
    for g in groc:
        print(g[0] + " X", g[1], g[1]*g[2])
    print("Subtotal:", sub, "\tTax:", "{:.2f}".format(tax))
    print("Total:", "{:.2f}".format(total))

def checkout(groceries, taxrate = 0.0975):
    sub = 0
    for g in groceries:
        sub += g[2] * g[1]   # Price * Quantity
    tax = sub * taxrate
    total = sub + tax
    printReceipt(groceries, sub, tax, total)

def main():
    groceries = []
    while True:
        item = getGroceryItem()
        if item is None:
            break
        groceries.append(item)
    checkout(groceries)
main()