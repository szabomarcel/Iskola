sorszamok_string = ["első", "második", "harmadik"]
szamok = []
for i in sorszamok_string:
   szamok.append(float(input(f"Írja be a(z) {i} oldalt: ")))

a = 0
b = 0
c = 0
index = 0
for i in szamok:
   if c < i:
      c = i

for i in szamok:
   if i != c:
      if index == 0:
         a = i
         index += 1
      else:
         b = i

q = (a**2)+(b**2)
if q >= c**2 - 0.001 and q <= c**2 + 0.001:
   print("A háromszög derékszög!")
else: print("A háromszög nem derékszög!")