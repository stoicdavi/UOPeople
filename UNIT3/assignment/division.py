while True:
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    if num2 == 0:
        print('Error! Division by zero not allowed!')
    else:
        print(f'{num1} divided by {num2} is {num1/num2}')
    again = input('Do you want to divide again? (yes or no): ')
    if again.lower() != 'yes':
        break
print('Goodbye!')