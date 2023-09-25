# Program #4:
def convertMillis(millis):
    hrs = millis // 3600000
    mins = (millis % 3600000) // 60000
    secs = (millis % 3600000) % 60000
    secs = secs // 1000
    return str(hrs) + ":" + str(mins) + ":" + str(secs)


m = int(input("Enter time in milliseconds: "))
print(convertMillis(m))