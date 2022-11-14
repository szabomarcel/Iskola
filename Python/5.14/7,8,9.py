import turtle

class Rajz:
   width = -160
   def szamozas():
      y = 190
      for i in range(0,39):
         t.goto(-180,y)
         t.goto(-175,y)
         t.goto(-185,y)
         t.goto(-180,y)
         y -= 10

   def diagram(height):
      color = ""
      if height >= 200:
         color = "red"
      elif height < 200 and height >= 100:
         color = "yellow"
      elif height < 100:
         color = "green"
      
      t.goto(Rajz.width,0)
      
      t.pendown()
      t.fillcolor(color)
      t.begin_fill()
      t.goto(Rajz.width,height)
      t.goto(Rajz.width + 10,height)
      t.goto(Rajz.width + 10,0)
      t.end_fill()
      t.penup()
      Rajz.width += 20

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(100)

t.goto(200,0)
t.goto(-200,0)
t.goto(-180,0)
t.goto(-180,200)
t.goto(-180,-200)
Rajz.szamozas()
t.penup()

for i in range(0,int(input("Írd be hány darab grafikob lesz: "))):
   Rajz.diagram(int(input(f"Írd be az {i + 1}. grafikon nagyságát: ")))

screen.mainloop()