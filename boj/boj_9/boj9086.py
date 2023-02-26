import sys
for _ in range(int(sys.stdin.readline())):
    string = sys.stdin.readline().rstrip()
    print(string[0], end='')
    print(string[-1])