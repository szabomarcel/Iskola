import random

tabla = []

for i in range(100):
   tabla.append(random.randint(-100,100))

def negativ_plus(szamok):
   osszeg = 0
   for szam in szamok:
      if szam < 0:
         osszeg += szam
   return osszeg

print(negativ_plus(tabla))