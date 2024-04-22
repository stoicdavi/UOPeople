import math # import math module
pi = round(math.pi, 5) #set pi as a global variable
def print_circum(radius): 
     circum = 2 * pi * radius
     print(f"The Circumference is {circum}")
#function call
print_circum(7)
