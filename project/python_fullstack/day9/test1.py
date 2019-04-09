with open("d.txt", 'rb') as f:
    f.seek(-5,2)
    print(f.tell())
    print(f.readline())

