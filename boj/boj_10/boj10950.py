import sys
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    a, b = [int(num) for num in sys.stdin.readline().rstrip().split()]
    print(a + b)