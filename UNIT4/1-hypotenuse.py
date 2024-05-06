import math as m
def hypotenuse_len(base, height):
    hypotenuse = m.sqrt(base ** 2 + height ** 2)
    return hypotenuse
print('Enter the base and height of the right triangle to calculate the hypotenuse')
b = int(input("Enter the base: "))
h = int(input("Enter the height: "))
print(hypotenuse_len(b, h))
