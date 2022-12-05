égtájak = [ "É", "K", "D", "Ny" ]

def fordulj_orajarasi_iranyba(egtaj):
   egtaj = egtaj.lower()
   if egtaj == "é":
      return "K"
   elif egtaj == "k":
      return "D"
   elif egtaj == "d":
      return "Ny"
   elif egtaj == "ny":
      return "É"
   else:
      return None


print("A következő égtáj órajárásban", fordulj_orajarasi_iranyba(input("Írd be a jelenlegi égtájat: ")))