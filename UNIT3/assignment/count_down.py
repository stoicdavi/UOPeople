
def countUp(n):
    '''Count up from -n to 0 and then print Blast off!'''
    if n == 0:
        print('Blast off!')
    else: 
        print(n)
        countUp(n+1)

def countDown(n):
    '''Count down from n to 0 and then print Blast off!'''
    if n >= 0:
        print(n)
        countDown(n-1)
    else:
        print('Blast off!')

number = int(input('Enter a number: '))
if number <= 0:
    countUp(number)
else:
    countDown(number)