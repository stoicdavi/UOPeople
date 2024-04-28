import turtle


def Star(t, n, length):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
    turtle.mainloop()


p = turtle.Turtle()
n = int(input("Enter the number of sides for your polygon: "))
length = int(input("Enter the length of the sides of your polygon: "))
Star(p, n, length)
