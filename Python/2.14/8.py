format = True

while format:
   try:
      jelenlegiIdo = int(input("Írd be a jelenlegi időt (órában megadva): "))
      format = False
   except:
      print("Nem megfelelő formátum!")

format = True

while format:
   try:
      csengetes = int(input("Írd be, hogy hány óra múlva csengessen az óra (órában megadva): "))
      format = False
   except:
      print("Nem megfelelő formátum!")

for i in range(0, csengetes):
   if jelenlegiIdo == 23:
      jelenlegiIdo = 0
   else:
      jelenlegiIdo += 1
      
print(jelenlegiIdo,"órakkor fog megszólalni a csengő.")