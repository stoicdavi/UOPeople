
def strings():
    # Asking user to enter his/her name
    n = input('Enter your name: ')
    #length of the name using len() function
    name_len = len(n)
    print('Your name is : ', n)
    print('Length of your name is : ', name_len)
    #printing the name in revers using slicing technique
    print(n[::-1])
    # using for loop to revers the the input name
    print('Using for loop to reverse string')
    for i in range(name_len-1, -1, -1):
        print(n[i], end='')
    # using while loop to revers the the input name
    print()
    index = name_len-1
    print('Using while loop')
    while index >= 0:
        print(n[index], end='')
        index -= 1
    print()
    # Counting the number of vowels in the input string
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    for char in n:
        if char in vowels:
            vowel_count += 1
    print('Number of vowels in your name:', vowel_count)
strings()