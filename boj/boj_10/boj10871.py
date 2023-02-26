import sys
x = int(sys.stdin.readline().rstrip().split()[1])
a = [int(num2) for num2 in sys.stdin.readline().rstrip().split()]
for result in list(filter(lambda y: y<x, a)):
    print(result, end=' ')