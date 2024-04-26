from function_to_draw_grid import print_grid
def print_modified_grid():
    print("using imported module function_to_draw_grid.py")
    print(print_grid())
    #drawing grid with 5x5
    print("+ - - - - + - - - - + - - - - + - - - - +")
    print(("|         |         |         |         |\n") *4, end="")
    print("+ - - - - + - - - - + - - - - + - - - - +")
    print(("|         |         |         |         |\n") *4, end="")
    print("+ - - - - + - - - - + - - - - + - - - - +")

print_modified_grid()