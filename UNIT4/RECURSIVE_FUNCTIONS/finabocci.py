def fibonacci_num(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_num(n-1) + fibonacci_num(n-2)
num = int(input("Enter a number: "))
print(f'The fibonacci of {num} is {fibonacci_num(num)}')