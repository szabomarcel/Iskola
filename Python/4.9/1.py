import turtle

screen = turtle.Screen()
teknos = turtle.Turtle()

class Forma:
   def Négyzet():
      turtle.pendown()
      for x in range(0,4):
         turtle.left(90)
         turtle.forward(20)
      turtle.penup()

for x in range(0,5):
   Forma.Négyzet()
   turtle.forward(40)

screen.mainloop()