from classes import Téglalap

t1 = Téglalap()
t1.SetA(int(input("Írd be a téglalap \"a\" oldalát: ")))
t1.SetB(int(input("Írd be a téglalap \"b\" oldalát: ")))
print("A t1 kerülete: {0}. Területe: {1}".format(t1.GetKerület(), t1.GetTerület()))