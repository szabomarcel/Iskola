def karakter_szamlalas(szoveg, karakter):
   darab = 0
   for sz in szoveg:
      if sz == karakter:
         darab += 1
   return darab

print(karakter_szamlalas("alma", "a"))