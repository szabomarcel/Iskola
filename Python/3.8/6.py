import turtle

screen = turtle.Screen()
teknos = turtle.Turtle()
class Teknös:
   def Kiiras(hanyszor, fok):
      screen.clear()
      teknos = turtle.Turtle()
      for i in range(0, hanyszor):
         teknos.left(fok)
         teknos.forward(100)



Teknös.Kiiras(3,120)
Teknös.Kiiras(4,90)
Teknös.Kiiras(6,60)
Teknös.Kiiras(8,45)

screen.mainloop()