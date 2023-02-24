from sys import stdin

queue = []
for _ in range(int(stdin.readline().rstrip())):
    command = stdin.readline().rstrip()
    if command[:4] == 'push':
        queue.append(int(command[5:]))
    elif command == 'pop':
        try:
            print(queue[0])
            del queue[0]
        except IndexError:
            print(-1)
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        print(int(not queue))
    elif command == 'front':
        try:
            print(queue[0])
        except IndexError:
            print(-1)
    else:
        try:
            print(queue[-1])
        except IndexError:
            print(-1)