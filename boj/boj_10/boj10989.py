import sys
lst = [0] * 10000
for _ in range(int(sys.stdin.readline())):
    lst[int(sys.stdin.readline())-1] += 1
for i in range(10000):
    for _ in range(lst[i]):
        print(i+1)
