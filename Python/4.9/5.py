import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(100)
hossz = 1

for i in range(0, 100):
   t.forward(hossz)
   t.right(90)
   hossz += 1


screen.clear()
t = turtle.Turtle()
szög = 91
hossz = 10
t.speed(100)

for i in range(0, 100):
   t.forward(hossz)
   t.left(szög)
   hossz += 1

screen.mainloop()