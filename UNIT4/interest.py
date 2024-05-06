def simple_int(principal, rate, time):
    return (principal * rate * time) / 100
while True:
    try:
        p = int(input("Enter the principal amount: "))
        r = int(input("Enter the rate of interest: "))
        t = int(input("Enter the time: "))
        print(simple_int(p, r, t))
        choice = input('Do you want to calculate another interest? (y/n): ')
        if choice.lower() != 'y':
            break
    except ValueError:
        print('Please enter a valid number')

