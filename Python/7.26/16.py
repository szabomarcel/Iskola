def negyzetosszeg(xs):
   n = 0
   for x in xs:
      n = n + x*x
   return n

print(negyzetosszeg([2,3,4]))