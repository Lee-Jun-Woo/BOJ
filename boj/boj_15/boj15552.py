import sys
a = int(sys.stdin.readline().rstrip())
for i in range(a):
    b, c = sys.stdin.readline().rstrip().split()
    b, c = int(b), int(c)
    print(b+c)