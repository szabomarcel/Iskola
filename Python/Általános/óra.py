import turtle
from time import *

screen = turtle.Screen()
t = turtle.Turtle()
t.pensize(3)
t.penup()
t.speed(0)

for i in range(12):
   t.forward(100)
   t.pendown()
   t.forward(1)
   t.penup()
   t.back(101)
   t.right(30)

screen.mainloop()