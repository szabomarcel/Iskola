import calendar
import os
naptar = calendar.LocaleTextCalendar(calendar.MONDAY, "HUNGARIAN")
for x in range(12):
   os.system("color 0f")
   if x + 1 == 9:
      os.system("color 0a")
   naptar.prmonth(2017, x + 1, 1, 1)
   print("\n")

# A calendar.isleap() függvény megvizsgálja, hogy az év szökőév-e