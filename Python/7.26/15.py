def paros_szamjegy_szam(n):
   t = []
   index = 0
   for i in range(len(n)):
      if int(n[i])%2==0:
         index += 1
   return index
print(paros_szamjegy_szam(input()))