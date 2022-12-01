import random

szamok = []

for i in range(100):
   szamok.append(random.randint(0,100))

def paratlan_e(tabla):
   paratlanok = 0
   for szam in tabla:
      if szam % 2 == 1:
         paratlanok += 1
   return paratlanok

print(paratlan_e(szamok))