napok = [ "Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap" ]

napIn = input().lower()
napIndex = None

for i in range(0, len(napok)):
   if napIn == napok[i].lower():
      napIndex = i

print(napIndex)