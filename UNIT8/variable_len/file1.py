with open('words.txt', 'r') as fin:
    f_contents = fin.readline()
    print(f_contents)

with open('words.txt', 'r') as fin:
    f_contents = fin.readlines(10) # reads 10 the lines
    print(f_contents)

with open('words.txt', 'r') as fin:
    f_contents = fin.readlines(19) # reads all the lines
    print(f_contents)


with open('test.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('R')
    
    with open('test.txt', 'r') as rf:
        print(rf.read())