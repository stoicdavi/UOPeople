print("\t***WELCOME TO OUR VOTING SYSTEM***\n\nPlease ", end='')
name = input("Enter Your name: ")
age  = int(input('Enter your age: '))
country = input('Enter your country name: ')
votingAge = 18
if age >= votingAge:
    if country == 'Kenya':
        print(f'Congratulations {name}, You are a qualified voter')
    else:
        print(f"Sorry {name}, You are a qualified voter but not in Kenya")
else:
    if country == 'Kenya':
        print('Sorry ' + name + " You have " + str(votingAge - age) + ''' Years remaining 
              before you become a 
              qualified voter''')
    else:
        print(f"Sorry {name}, You must be a Kenyan Citizen and {votingAge} years and above")
