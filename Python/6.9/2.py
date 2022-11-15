napok = [ "Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap" ]

try:
   napIndex = int(input("Írja be a nap számát (0-6): "))
   if napIndex >= 0 and napIndex <= 6:
      print(napok[napIndex])
   else:
      print(None)
except:
   print("Nem helyes formátum!")