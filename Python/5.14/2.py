napok = [ "Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap" ]
napIndex = 2

for i in range(2, 137):
   if napIndex != 6:
      napIndex += 1
   else:
      napIndex = 0

print(f"{137 - 3} éjszát voltál ott és {napok[napIndex]}i napon jössz haza.")