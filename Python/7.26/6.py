def szamol_nem(szoveg):
   szavak = szoveg.split(" ")
   szam = 0
   done = False
   for szo in szavak:
      if not done:
         if szo != "nem":
            szam += 1
         else:
            szam += 1
            done = True
   return szam
