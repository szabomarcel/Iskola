import time
import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.color("black")
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

t.left(90)
t.pendown()
t.hideturtle()

while True:
   t.color("black")
   t.forward(90)
   t.back(90)
   time.sleep(1)
   t.color("white")
   t.forward(90)
   t.back(90)
   t.right(6)