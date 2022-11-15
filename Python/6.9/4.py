napok = [ "Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap" ]
napIndex = 0

def NyaraloSzamolas(napNev, napQ):
   napIndex = 0
   for i in range(0, len(napok)):
      if napNev == napok[i].lower():
         napIndex = i
   for i in range(0, napQ):
      if napIndex == 6:
         napIndex = 0
      else: napIndex += 1
   return napok[napIndex]

nyaraloNap = NyaraloSzamolas(input("Írd be a mai napot: "), int(input("Hány nap múlva mész nyaralni?: ")))
print(f"{nyaraloNap}-n fogsz menni nyaralni!")