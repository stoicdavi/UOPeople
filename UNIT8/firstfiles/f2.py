with open('text2.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('R')

with open('text2.txt', 'r') as f:
    print(f.read())