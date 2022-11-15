class Ido:
   def orara_valtas(masodpercek):
      marms = masodpercek
      ora = int(round(marms / 3600, 0))
      marms = marms % 3600
      perc = int(round(marms / 60, 0))
      marms = marms % 60
      masodperc = int(marms)
      
      ido = [ora, perc, masodperc]
      return ido
      
   def percre_valtas(masodpercek):
      marms = masodpercek
      perc = int(round(marms / 60, 0))
      marms = marms % 60
      masodperc = int(marms)
      ido = [perc, masodperc]
      return ido
      
   def masodpercre_valtas(masodpercek):
      ido = Ido.percre_valtas(masodpercek)
      return ido

print(Ido.orara_valtas(9010)[0],"óra",Ido.orara_valtas(9010)[1],"perc",Ido.orara_valtas(9010)[2],"másodperc")
print(Ido.percre_valtas(9010)[0])
print(Ido.masodpercre_valtas(9010))