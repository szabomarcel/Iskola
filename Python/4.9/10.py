import turtle

screen = turtle.Screen()
t = turtle.Turtle()

t.left(35)
for i in range(0,5):
   for i in range(0,5):
      t.forward(100)
      t.left(144)
   t.penup()
   t.forward(650)
   t.right(144)
   t.pendown()

screen.mainloop()

# Ugyan úgy mint az alap csillag