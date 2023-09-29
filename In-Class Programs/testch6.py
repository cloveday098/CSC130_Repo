s1 = "hello"
s2 = "world"
s3 = ""
for i in range(min(len(s1), len(s2))):
    s3 += s1[i] + s2[i]
if min(len(s1), len(s2)) == len(s1):
    s3 += s2[len(s1):]
else:
    s3 += s1[len(s2):]
print(s3)