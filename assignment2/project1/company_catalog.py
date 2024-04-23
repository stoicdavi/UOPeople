def Company_catalog():
    selected_items = []  # List to store selected choices
    while True:
        try:
            print("\nOnline Store \n----------------------------")
            print("""
            Product(s)              Price
            Item 1                  200.0
            Item 2                  400.0
            Item 3                  600.0
            Combo 1(Item 1 + 2)     540.0
            Combo 2(Item 2 + 3)     900.0
            Combo 3(Item 1 + 3)     720.0
            Combo 4(Item 1 + 2 + 3) 900.0""")
            print("________________________\nFor delivery Contact: 0721823498\n")
            choice = input("Select your gift 1 - 3, c1 - c4 or q to quit: ")
            if choice == '1':
                selected_items.append(200)
            elif choice == '2':
                selected_items.append(400)
            elif choice == '3':
                selected_items.append(600)
            elif choice == 'c1':
                selected_items.extend([200, 400])
            elif choice == 'c2':
                selected_items.extend([400, 600])
            elif choice == 'c3':
                selected_items.extend([200, 600])
            elif choice == 'c4':
                selected_items.extend([200, 400, 600])
            elif choice == 'q':
                print("Thank you for shopping with us")
                break  # Exit the loop and quit the program
            else:
                print("Invalid choice, try again")
                continue
            total_price = sum(selected_items)
            print(f'\n***Your total charge is {total_price} shillings only****')
        except:
            print("Invalid choice")
            continue
    
Company_catalog()

