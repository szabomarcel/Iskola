import math

c = 10000   # alaptőke
r = 0.08    # névleges kamatláb
m = 12     # évközi kamatozások száma
t = int(input("Írd be hány évre szeretnéd a kamatozást: ")) # futamidő

fv = (c * ((1 + r / m) ** (m * t)))

print("A betét értéke:", fv)