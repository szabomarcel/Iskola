napok = [ "Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap" ]

def nap_nev(n):
   n = int(n)
   if n >= 0 and n <= 6:
      return napok[n]
   else: return None

print(nap_nev(input()))