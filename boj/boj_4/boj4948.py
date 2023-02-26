# 베르트랑 공준
from sys import stdin
while True:
    n = int(stdin.readline())
    if not n: break # n이 0일 때 종료
    result = 0
    for i in range(n+1, 2*n+1):
        max = int(i ** 0.5) + 1
        for j in range(2, max):
            if not (i % j): break
        else:
            result += 1
    print(result)