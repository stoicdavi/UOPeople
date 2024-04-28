import turtle
p = turtle.Turtle()
def Star(t, length):
    i = 0
    while i < 8:
        t.fd(length)
        t.lt(135)
        i += 1
    turtle.mainloop()
Star(p, 100)