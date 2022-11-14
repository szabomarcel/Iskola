napok = [ "Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap" ]

try:
   napIndex = int(input("Írja be a nap számát (1-7): "))
   print(napok[napIndex - 1])
except:
   print("Nem helyes formátum!")