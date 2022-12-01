import random

szamok = []

for i in range(100):
   szamok.append(random.randint(0,100))

def paros_plus(tabla):
   osszeg = 0
   for szam in tabla:
      if szam % 2 == 0:
         osszeg += szam
   return osszeg

print(paros_plus(szamok))