def Company_catalog():
    print("Online Store \n----------------------------")
    print("""Product(s)              Price
    Item 1                  200.0
    Item 2                  400.0
    Item 3                  600.0
    Combo 1(Item 1 + 2)     540.0
    Combo 2(Item 2 + 3)     900.0
    Combo 3(Item 1 + 3)     720.0
    Combo 4(Item 1 + 2 + 3) 900.0""")

    print("________________________\nFor delivery Contact: 0721823498")
    choice = input("Select your gitf 1 - 3, c1 - c4: ")
    if choice == '1':
        price = 200
    elif choice == '2':
        price = 400
    elif choice == '3':
        price = 600
    elif choice == '4':
        price = 540 - (0.1 * 540)
    elif choice == '5':
        price = 900 - (0.1 * 900)
    elif choice == '6':
        price = 720 - (0.1 * 720)
    elif choice == '7':
        price = 900 - (900 * 0.25)
    else:
        print("Invalid choice")
    print(f'\nYour total charge is {price} shillings only')

Company_catalog()
