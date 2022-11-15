a = 0
b = 0

isDone = True
while isDone:
   try:
      a = int(input("Írja be az első befogót hosszát (cm): "))
      b = int(input("Írja be a második befogót hosszát (cm): "))
      isDone = False
   except:
      print("Rossz adatbevitel!")

print(f"A derkészögű háromszög átfogója {(((a*a) + (b*b)) ** 0.5)}cm.")