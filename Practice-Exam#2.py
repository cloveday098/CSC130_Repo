price = float(input("Enter the purchase price of the vehicle: "))

rate = 0.15

currentValue = price

print("Year\tExpected Value")
print("-" * 20)

for year in range(1, 6):
    depreciation = currentValue * rate
    
    currentValue -= depreciation
    
    print(f"{year}\t${currentValue:.2f}")

