import turtle


def Square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()


bob = turtle.Turtle()
length = int(input("Enter the length of the square You want to draw: "))
Square(bob, length)
