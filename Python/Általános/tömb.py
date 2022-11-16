import random

t = []
for i in range(0,5):
   t.append(random.randint(1,100))
print(t)

összeg = 0
for i in t:
   összeg += i
print(összeg)
atl = összeg / len(t)
print(atl)

def Mini(tömb):
   legkisebb = tömb[0]
   for i in tömb:
      if i < legkisebb:
         legkisebb = i
   return legkisebb

def Maxi(tömb):
   legnagyobb = tömb[0]
   for i in tömb:
      if i > legnagyobb:
         legnagyobb = i
   return legnagyobb

print(Mini(t))
print(Maxi(t))
