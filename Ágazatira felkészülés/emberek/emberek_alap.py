import random

class Ember():
    def __init__(self, nev, foglalkozas, nem):
        self.nev = nev
        self.foglalkozas = foglalkozas
        self.nem = nem
        self.szerencseszam = random.randint(1, 50)
        
    
    def neme(self):
        if self.nem == "f":
            return "Férfi"
        else:
            return "Nő"