from sys import stdin

stack = []
for _ in range(int(stdin.readline().rstrip())):
    command = stdin.readline().rstrip()
    if command[:4] == 'push':
        stack.append(int(command[5:]))
    elif command == 'pop':
        try:
            print(stack.pop())
        except IndexError:
            print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        print(int(not stack))
    else:
        try:
            print(stack[-1])
        except IndexError:
            print(-1)