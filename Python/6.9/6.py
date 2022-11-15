hónapokNapja = [ 30, 28, 30, 31, 30, 31, 30, 31, 30, 31, 30, 31 ]
hónapok = [ "Január", "Február", "Március", "Április", "Május", "Június", "Július", "Augusztus", "Szeptember", "Október", "November", "December" ]

def honap_napja(hónapIn):
   index = 0
   for i in range(0, len(hónapok)):
      if hónapok[i].lower() == hónapIn:
         index = i
   return hónapokNapja[index]

inp = input("Írd be a hónap napját: ").lower()
print("Ez a hónap",honap_napja(inp),"napos")