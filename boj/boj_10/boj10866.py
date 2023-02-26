from sys import stdin
from collections import deque as deq

deque = deq()
for _ in range(int(stdin.readline().rstrip())):
    command = stdin.readline().rstrip()
    if command[:10] == 'push_front':
        deque.appendleft(int(command[11:]))
    elif command[:9] == 'push_back':
        deque.append(int(command[10:]))
    elif command[:9] == 'pop_front':
        try:
            print(deque.popleft())
        except IndexError:
            print(-1)
    elif command[:8] == 'pop_back':
        try:
            print(deque.pop())
        except IndexError:
            print(-1)
    elif command == 'size':
        print(len(deque))
    elif command == 'empty':
        print(int(not deque))
    elif command == 'front':
        try:
            print(deque[0])
        except IndexError:
            print(-1)
    else:
        try:
            print(deque[-1])
        except IndexError:
            print(-1)