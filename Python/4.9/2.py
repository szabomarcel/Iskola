import turtle

screen = turtle.Screen()
teknos = turtle.Turtle()
szélesség = 20

class Forma:
   def Rajzol():
      teknos.pendown()
      for i in range(0,4):
         teknos.left(90)
         teknos.forward(szélesség)
      teknos.penup()
   def ÚjNégyzet():
      for i in range(0,2):
         teknos.right(90)
         teknos.forward(10)
      teknos.right(180)

for i in range(0,5):
   Forma.Rajzol()
   teknos.
   szélesség += 20