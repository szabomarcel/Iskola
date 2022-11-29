#1
"""
a = int(input("A: "))
b = int(input("B: "))

if a < 0 and b < 0:
   print("Mind a két szám negatív!")
elif a >= 0 and b >= 0:
   print("Mind a két szám pozitív!")
elif a <= 0:
   print("Az első szám negatív!")
elif b <= 0:
   print("A második szám negatív!")
"""
#2
"""
def HoE(a):
   b = False
   if a > 150:
      b = True
   return b

cim = input("Cím: ")
oldalak = int(input("Oldalak: "))

if HoE(oldalak):
   print("A könyv hosszú")
else:
   print("A könyv rövid")
"""