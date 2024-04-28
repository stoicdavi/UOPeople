# A circle
import turtle
import math
def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)
def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
    turtle.mainloop()
p = turtle.Turtle()
r = int(input("Enter the radius of the circle You want to draw: "))
circle(p, r)
