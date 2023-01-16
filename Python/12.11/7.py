
"""
s = "Esik es ̋o csendesen, lepereg az ereszen..."
# Szavanként lebontja egy listára a mondatot
print(s.split())
# Ennek a listának a típusát mutatja meg (list)
print(type(s.split()))
# Minden e-nél elválasztja és úgy készít (szöveges) listát a szöveg-ből és az e betüket törli
print(s.split("e"))
# Ua. csak s betükkel
print(s.split("s"))
# Az e betük helyére 0-át rak
print("0".join(s.split("e")))
"""

def cserel(regi, uj, s):
   s = str(s)
   uj = str(uj)
   regi = str(regi)
   return uj.join(s.split(regi))