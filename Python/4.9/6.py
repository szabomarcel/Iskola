import turtle

def poligon_rajzolas(t, sz):
   n = 360/sz
   for i in range(0,int(n)):
      t.forward(50)
      t.left(sz)

screen = turtle.Screen()
teknos = turtle.Turtle()

poligon_rajzolas(teknos, 120)

screen.mainloop()