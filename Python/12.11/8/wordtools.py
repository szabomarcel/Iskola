def szo_tisztitas(string):
   special_characters = "\"!@#$%^&*():-+?_=,<>\\"
   special_characters = [*special_characters]
   for sc in special_characters:
      string = "".join(string.split(sc))
   return string

def van_duplavonal(string):
   return "--" in string

def szavakra_bontas(string):
   string = string.split()
   for x in range(len(string)):
      string[x] = string[x].lower()
   
def szavak_szama(string, list):
   index = 0
   for l in list:
      if l == string: index += 1
   return index

def szo_halmaz(list):
   van = []
   for l in list:
      if l not in van:
         van.append(l)
   return van

def leghosszabb_szo(list):
   leghosszabb = 0
   for l in list:
      if len(l) > leghosszabb:
         leghosszabb = len(l)
   return leghosszabb