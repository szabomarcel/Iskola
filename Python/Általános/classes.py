class Téglalap:
   def __init__(self, a = 0, b = 0):
      self.a = a
      self.b = b
   
   def SetA(self, a):
      self.a = a
   def SetB(self, b):
      self.b = b
   def SetAB(self, a, b):
      self.a = a
      self.b = b
   
   def GetA(self):
      return self.a
   def GetB(self):
      return self.b
   def GetKerület(self):
      return 2 * (self.a + self.b)
   def GetTerület(self):
      return self.a * self.b

class Négyzet:
   def __init__(self, a = 0):
      self.a = a
   
   def SetA(self, a):
      self.a = a
   
   def GetA(self):
      return self.a
   def GetKerület(self):
      return 4 * self.a
   def GetTerület(self):
      return self.a ** 2

class Kör:
   def __init__(self, r = 0):
      self.r = r
   
   def SetR(self, r):
      self.r = r
   
   def GetR(self):
      return self.r
   def GetKerület(self):
      return 2 * 3.14 * self.r
   def GetTerület(self):
      return (3.14 * (2 * self.r) ** 2) / 4

class TéglalapHasáb:
   def __init__(self, a = 0, b = 0, m = 0):
      self.a = a
      self.b = b
      self.m = m
   
   def SetA(self, a):
      self.a = a
   def SetB(self, b):
      self.b = b
   def SetM(self, m):
      self.m = m
   def SetABM(self, a, b, m):
      self.a = a
      self.b = b
      self.m = m
   
   def GetA(self):
      return self.a
   def GetB(self):
      return self.b
   def GetM(self):
      return self.m
   
   def GetFelület(self):
      return ((self.a * self.b) + (self.a * self.m) + (self.b * self.m)) * 2
   def GetTérfogat(self):
      return self.a * self.b * self.m

class Ember:
   def __init__(self, név = "Droid", nem = "Semleges"):
      self.név = név
      self.nem = nem
   
   def SetNév(self, név):
      self.név = név
   def SetNem(self, nem):
      self.nem = nem
   def SetNM(self, név, nem):
      self.név = név
      self.nem = nem
   
   def GetNév(self):
      return self.név
   def GetNem(self):
      return self.nem
   
   def Köszön(self):
      print(f"Szia én {self.név} vagyok!")

