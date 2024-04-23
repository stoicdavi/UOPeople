import math # import math module
pi = round(math.pi, 5) #set pi as a global variable
def print_circum(radius): 
     circum = 2 * pi * radius
     print(f"The Circumference is {circum}")
#function call
while True:
    try:
        radi = int(input("Enter the radius: "))
        print_circum(radi)
        choice = input("Do you want to try again? y/n: ")
        if choice.lower() == 'y':
          continue
        else:
          break
    except ValueError:
        print("Invalid input, try again")
        continue
    

