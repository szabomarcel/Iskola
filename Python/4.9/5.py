import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
hossz = 1

for i in range(0, 100):
   t.forward(hossz)
   t.right(90)
   hossz += 1


screen.clear()
t = turtle.Turtle()
szög = 91
hossz = 10
t.speed(0)

for i in range(200):
   t.forward(hossz)
   t.left(szög)
   hossz += 1
   szög += 1

screen.mainloop()