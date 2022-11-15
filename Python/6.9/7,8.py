def masodperc_valtas(ora, perc, masodperc):
   ido = 0
   ido = ido + ora * 60 * 60
   ido = ido + perc * 60
   ido = ido + masodperc
   return ido

print(masodperc_valtas(1.5,30.1,30.7))