def factorial(n):
    if n == 0:
        return 1
    else:
        recursive = factorial(n -1)
        result = recursive * n
        return result


print("Welcome to our factorial calculator ")
num = int(input("Enter a number: "))
print(f'The factorial of {num} is {factorial(num)}')
