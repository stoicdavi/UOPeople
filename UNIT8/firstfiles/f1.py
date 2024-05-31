
with open('index.txt', 'r') as f:
    size_to_read = 10
    read_content = f.read(size_to_read)
    print(f.tell())

    while len(read_content) > 0:
        print(read_content, end='==')
        read_content = f.read(size_to_read)
