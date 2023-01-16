import random

file = open("nsa\\ige.txt", "r", encoding = "utf-8")
lines = file.read()
file.close()
ige = lines.split(" ")
print(len(ige))
file = open("nsa\\melleknev.txt", "r", encoding = "utf-8")
lines = file.read()
file.close()
melleknev = lines.split(" ")
file  = open("nsa\\mgh.txt", "r", encoding = "utf-8")
lines = file.read()
file.close()
mgh = lines.split(" ")

nev = input("Ki? ")
hol = input("Hol? ")

ig = ige[random.randint(0, len(ige) - 1)]
m1 = melleknev[random.randint(0, len(melleknev) - 1)]
m2 = melleknev[random.randint(0, len(melleknev) - 1)]

print(m1, nev, ig, m2, hol)