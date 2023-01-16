table = []
lines = []
file = open("Python\\13.11\\3\\output.txt", "r")
for line in file:
   for l in line.split():
      lines.append(l)
   table.append(lines)
   lines = []
file.close()

doneTable = []
doneLines = []
index = 0
for i in range(len(table)):
   for j in range(len(table[i])):
      if index < 5 and j % 2 == 0:
         doneLines.append(table[i][(index + 1) * 2])
         index += 1
      else: doneLines.append(table[i][j])
      doneTable.append(doneLines)
   index = 0

file = open("Python\\13.11\\4\\output.txt", "w")
for lines in doneTable:
   for words in lines:
      file.write(f" {words}")
   file.write("\n")
file.close()