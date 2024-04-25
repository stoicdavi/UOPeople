import turtle
bob = turtle.Turtle()
def Square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

        t.fd(length)
        t.lt(90)

        t.fd(length)
        t.lt(90)

        t.fd(length)
        t.lt(90)
        turtle.mainloop()
Square(bob, 100)