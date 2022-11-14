import turtle

screen = turtle.Screen()
t = turtle.Turtle()

t.speed(10)

for i in range(0,20):
   t.forward(100)
   t.forward(-100)
   t.left(18)

t.left(9)
for i in range(0,5):
   t.penup()
   t.forward(140)
   t.left(135)
   t.pendown()
   for i in range(0,4):
      t.forward(200)
      t.left(90)
   t.penup()
   t.right(135)
   t.forward(-140)
   t.left(18)
screen.mainloop()