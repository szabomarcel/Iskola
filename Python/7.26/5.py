def elso_paros(szamok):
   done = False
   tabla = []
   for szam in szamok:
      if not done:
         if szam % 2 == 0:
            done = True
         else:
            tabla.append(szam)
   return tabla
