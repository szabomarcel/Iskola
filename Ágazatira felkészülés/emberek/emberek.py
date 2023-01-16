from emberek_alap import Ember
élőlények = []

for x in range(3):
    név = input("Add meg a nevet!")
    foglalkozás = input("Add meg a foglalkozását!")
    neme = input("Add meg a nemét (f/n)!")
    élőlények.append(Ember(név, foglalkozás, neme))

pointer = open("emberek_lista.txt", "w")
for élőlény in élőlények:
    print(f"{élőlény.nev} {élőlény.neme()}, {élőlény.foglalkozas}, szerencse száma a {élőlény.szerencseszam}")
    pointer.write(f"{élőlény.nev} {élőlény.neme()}, {élőlény.foglalkozas}, szerencse száma a {élőlény.szerencseszam} \n")
pointer.close()