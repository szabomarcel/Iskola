class TicTacToe:
   def egy_jatszma(felhasznalo_kezd):
      import random
      veletlen = random.Random()
      eredmeny = veletlen.randrange(-1,2)
      print("Felhasználó kezd={0}), Nyertes={1} ".format(felhasznalo_kezd, eredmeny))
      return eredmeny
   
   def főprogram():
      import random
      start = True
      jatekos = 0
      gep = 0
      dontetlen = 0
      output = True
      veletlen = False
      jatekok_szama = 0
      
      while output:
         jatekok_szama += 1
         if start:
            if random.randint(0,1) == 1:
               veletlen = True
         else:
            veletlen = not veletlen
         vegeredemeny = TicTacToe.egy_jatszma(veletlen)
         if vegeredemeny == -1:
            print("Te nyertél!")
            jatekos += 1
         elif vegeredemeny == 0:
            print("Döntetlen!")
            dontetlen += 1
         elif vegeredemeny == 1:
            print("Én nyertem!")
            gep += 1
         
         print(f"Játékos pontjai: {jatekos}, Gép pontjai: {gep}, Döntetlen: {dontetlen}")
         print(f"A játékos a játszmák {100 / jatekok_szama * jatekos}%-át megnyerte!")
         output = input("Szeretnél még egyet játszani? (i/n) ").lower()
         if output == "n":
            print("Köszönöm, hogy játszottál! Szia!")
            output = False