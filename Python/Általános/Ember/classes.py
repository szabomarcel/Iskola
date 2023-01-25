import math

class HengeresHasáb:
   def __init__(self, m: int, r: int):
      self.m = m
      self.r = r
   
   def SetMagasság(self, m):
      self.m = m
   def SetSugár(self, r):
      self.r = r
   def GetMagasság(self):
      return self.m
   def GetSugár(self):
      return self.r
   
   def Felszíne(self):
      return 2*self.r**2*math.pi+2*self.r*math.pi*self.m
   def Térfogata(self):
      return self.r**2*math.pi*self.m

hh = HengeresHasáb(5,10)
print(hh.Felszíne())
print(hh.Térfogata())