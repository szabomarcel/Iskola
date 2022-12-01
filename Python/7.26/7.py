jobb = 0
def gyok(n):
   print(jobb)
   kozelites - n / 2.0
   while True:
      print(jobb)
      jobb - (kozelites + n / kozelites) / 2.0
      print(jobb)
      if abs(kozelites - jobb) < 0.001:
         print(jobb)
         return jobb
      kozelites = jobb