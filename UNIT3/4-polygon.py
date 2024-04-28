import turtle
import math

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t, r, angle):
    if angle == 360:
        n = 100  # Increase the number of sides for a smoother circle
    else:
        n = int(angle / 3) + 1  # Approximation for the number of sides
    circumference = 2 * math.pi * r
    arc_length = circumference * (angle / 360)
    length = arc_length / n
    for _ in range(n):
        t.fd(length)
        t.lt(angle/n)

# Ask the user for the radius and number of angles
radius = int(input("Enter the radius: "))
angle = int(input("Enter the angle (360 for a complete circle): "))

# Test the circle function with user input values
p = turtle.Turtle()
p.speed(0)  # Set the turtle speed to the fastest
circle(p, radius, angle)

turtle.mainloop()
