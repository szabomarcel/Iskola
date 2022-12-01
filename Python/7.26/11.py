import turtle

def kaloz(t, tab):
   for v,k in tab:
      t.left(v)
      t.forward(k)

screen = turtle.Screen()
tek = turtle.Turtle()

table =  [(160, 20), (-43, 10), (270, 8), (-43, 12)]

kaloz(tek, table)

screen.mainloop()