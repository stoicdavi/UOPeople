import turtle


def polygon(ttl, length, n):
    for i in range(n):
        ttl.fd(length)
        ttl.lt(360/n)

    turtle.mainloop()


p = turtle.Turtle()
length = int(input("Enter the length of the polygon You want to draw: "))
n = int(input("Enter the number of sides of the polygon You want to draw: "))
polygon(p, length, n)
