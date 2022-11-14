import turtle

screen = turtle.Screen()
Eszti = turtle.Turtle()

def sokszog_rajzolas(t,n,sz):
   for i in range(0,n):
      t.left(sz)
      t.forward(50)


sokszog_rajzolas(Eszti, 8, 45)

screen.mainloop()