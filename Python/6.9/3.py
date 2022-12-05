napok = [ "Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap" ]

def nap_index(nap):
   nap = nap.lower()
   for i in range(0, len(napok)):
      if nap == napok[i].lower():
         return i
   return None

print(nap_index(input()))