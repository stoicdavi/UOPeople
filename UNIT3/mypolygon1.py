import turtle
p = turtle.Turtle()
def Star(t, n, length):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
    turtle.mainloop()


n = int(input("Enter the number of sides for your polygon: "))
angle = int(input("Enter the angle for your polygon: "))
Star(p, n, angle)