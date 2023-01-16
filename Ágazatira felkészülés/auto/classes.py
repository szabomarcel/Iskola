class Menetlevél:
    def __init__(self, rendszam):
        self.rendszam = rendszam
    
    def setMegtettKm(self, megtettkm):
        self.megtettkm = megtettkm
    def setÖsszÜzemanyag(self, összüzemanyag):
        self.összüzemanyag = összüzemanyag
    
    def atlagfogyasztas(self):
        atlag = self.összüzemanyag / (self.megtettkm / 100)
        return round(atlag, 2)
    
    def getrendszam(self):
        return self.rendszam