import turtle
p = turtle.Turtle()
def Star(t, n, length):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
      
    turtle.mainloop()
Star(p, 9, 90)