def ezOtBetusQ(szavak):
   szam = 0
   for szo in szavak:
      if szo.len() == 5:
         szam += 1
   return szam