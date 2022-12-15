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