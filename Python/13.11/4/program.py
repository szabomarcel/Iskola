table = []
lines = []
file = open("Python\\13.11\\3\\output.txt", "r")

for line in file:
   for l in line.split():
      lines.append(line)
   table.append(lines)
   lines = [] 
file.close()

index = 0
col_index = 0
for i in range(len(table)):
   for j in range(len(table[i])):
      if index < 5 and j % 2 == 0:
         table[i].remove(table[i][index * 2])
         index += 1
   index = 0

file = open("Python\\13.11\\4\\output.txt", "w")
for t in table:
   for line in t:
      file.write(f"{line} ")
   file.write("\n")
file.close()