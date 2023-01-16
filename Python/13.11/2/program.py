lines = []
file = open("Python\\13.11\\2\\input.txt", "r")
for line in file:
   lines.append(line[:len(line)-1])
file.close()

for line in lines:
   if "info" in line:
      print(line)