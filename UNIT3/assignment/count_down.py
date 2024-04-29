
def countUp(n):
    '''Count up from n to 0'''
    if n == 0:
        print('Blast off!')
    else: 
        print(n)
        countUp(n+1)
num = int(input('Enter a number: '))
countUp(num)
