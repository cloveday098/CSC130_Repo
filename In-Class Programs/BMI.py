w = int(input("Weight in pounds: "))
h = int(input("Height in meters: "))
w /= 2.205
h /= 39.37
BMI = w/(h**2)
print(BMI)
if (BMI < 18.5):
    print("Underweight")
elif (BMI < 25):
    print("Normal")
elif (BMI < 30):
    print("Overweight")
else:
    print("Obese")