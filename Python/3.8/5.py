import math

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for i in xs:
   print(i)

for i in xs:
   print(i)
   print(i * i)

összeg = 0

for i in xs:
   összeg += i

print(összeg)
összeg = 1

for i in xs:
   összeg = összeg * i

print(összeg)