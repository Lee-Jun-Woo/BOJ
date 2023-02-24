for _ in range(int(input())):
    data = input().split()
    r = int(data[0])
    for char in data[1]:
        print(char*r, end='')
    print()