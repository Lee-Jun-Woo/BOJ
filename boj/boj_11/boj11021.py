import sys
t = int(sys.stdin.readline().rstrip())
for i in range(1, t+1):
    a, b = sys.stdin.readline().rstrip().split()
    a, b = int(a), int(b)
    print('Case #%d:' % i, end=' ')
    print(a+b)