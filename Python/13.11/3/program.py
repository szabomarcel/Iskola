table = []
file = open("Python\\13.11\\3\\input.txt", "r")

for line in file:
   lines = line.split()
   table.append(lines)
file.close()

index = 0.001
col_index = 0
emptystring = ""
file = open("Python\\13.11\\3\\output.txt", "w")
for t in table:
   for l in t:
      if col_index < 5:
         file.write(f" {emptystring.join(str(index).split('.'))[:4]} {l}")
         index += 0.001
         col_index += 1
      else:
         file.write(f" {l}")
   col_index = 0
   file.write("\n")
file.close()