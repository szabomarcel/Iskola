égtájak = [ "É", "K", "D", "Ny" ]
következő = ""

def fordulj_orajarasi_iranyba(egtaj):
   if egtaj == "é":
      következő = "Kelet"
   elif egtaj == "k":
      következő = "Dél"
   elif egtaj == "d":
      következő = "Nyugat"
   elif egtaj == "ny":
      következő = "Észak"
   else:
      következő = None
   return következő


print("A következő égtáj órajárásban", fordulj_orajarasi_iranyba(input("Írd be a jelenlegi égtájat: ").lower()))