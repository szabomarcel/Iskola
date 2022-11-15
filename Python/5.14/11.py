a = 0
b = 0
c = 0

isDone = True
while isDone:
   try:
      a = int(input("Írja be a háromszög 1. oldalát: "))
      b = int(input("Írja be a háromszög 2. oldalát: "))
      c = int(input("Írja be a háromszög 3. oldalát: "))
      isDone = False
   except:
      print("Rossz adatbevitel!")

if abs()