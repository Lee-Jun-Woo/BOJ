import sys
a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
c = int(sys.stdin.readline().rstrip())
mul = str(a * b * c)
for i in range(10):
    print(mul.count(str(i)))