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

#3
import random

class Szere:
   def __init__(self, nev, fog, nem, szam):
      self.nev = nev
      self.fog = fog
      self.nem = nem
      self.szam = szam
   
   def FvN(nem):
      if nem.lower() == "f": return "Férfi"
      elif nem.lower() == "n": return "Nő"

t = []
for x in range(3):
   a = input("Add meg a nevet: ")
   b = input("Add meg a nemet (f/n): ")
   c = input("Add meg a foglalkozást: ")
   d = random.randint(1,50)
   t.append(Szere(a,b,c,d))

for x in t:
   print(x.nev)