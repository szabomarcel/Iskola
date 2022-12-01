"""
a = int(input("Szám: "))
b = int(input("Szám: "))

if a < b:
   print(f"A {b} nagyobb mint az {a}!")
elif a > b:
   print(f"Az {a} nagyobb mint a {b}!")
else:
   print("A két szám egyforma!")
"""
   
def MagasE(magassag):
   if magassag < 170: return False
   else: return True

nev = input("Név: ")
while nev != "":
   m = int(input("Magasság: "))
   if MagasE(m): print(f"{nev} magasabb mint az átlag!")
   else: print(f"{nev} nem magasabb mint az átlag!")
   nev = input("Név: ")