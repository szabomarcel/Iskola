def szamjegy_szam(n):
   n = int(n)
   if n < 0:
      return len(str(n)) - 1
   else: return len(str(n))

print(szamjegy_szam(input()))