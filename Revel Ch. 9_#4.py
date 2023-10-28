# Program #4:

r1 = float(input("Enter the real part of the first complex number: "))
i1 = float(input("Enter the imaginary part of the first complex number: "))
r2 = float(input("Enter the real part of the second complex number: "))
i2 = float(input("Enter the imaginary part of the second complex number: "))

print("(" + str(r1), "+", str(i1) + "i) + (" + str(r2), "+", str(i2) + "i) = (" + str(r1+r2), "+", str(i1+i2) + "i)")
print("(" + str(r1), "+", str(i1) + "i) - (" + str(r2), "+", str(i2) + "i) = (" + str(r1-r2), "+", str(i1-i2) + "i)")
if (r1*i2 + r2*i1) > 0:
    print("(" + str(r1), "+", str(i1) + "i) * (" + str(r2), "+", str(i2) + "i) = (" + str("{:.2f}".format((r1+i1*1j)*(r2+i2*1j))).replace("j", "i").replace('-', ' + -', 2).replace('+', ' + ', 1) + ")")
else:
    print("(" + str(r1), "+", str(i1) + "i) * (" + str(r2), "+", str(i2) + "i) = (" + str("{:.2f}".format((r1 + i1 * 1j) * (r2 + i2 * 1j))).replace("j", "i").replace('-', ' + -', 2).replace(' + ', '', 1) + ")")
print("(" + str(r1), "+", str(i1) + "i) / (" + str(r2), "+", str(i2) + "i) = " + str((r1+i1*1j)/(r2+i2*1j)).replace('j', 'i').replace('-', ' + -', 2).replace(' + ', '', 1))
print("|(" + str(r1), "+", str(i1) + "i)| =", str(abs(r1 + i1*1j)))