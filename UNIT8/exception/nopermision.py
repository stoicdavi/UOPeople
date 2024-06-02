try:
    with open('../variable_len/test.txt', 'w') as f:
        f.write('Test')
except PermissionError:
    print('You do not have permission to write to this file')
finally:
    with open('../variable_len/test.txt', 'r') as f:
        print(f.read())