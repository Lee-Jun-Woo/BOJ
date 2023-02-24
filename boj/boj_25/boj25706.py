n = int(input())
road = tuple(map(int, input().split()))
res = [0] * n
for i in range(n-1, -1, -1):
    if (i + road[i] + 1) >= n:
        res[i] = 1
    else:
        res[i] = res[(i + road[i] + 1)] + 1
for j in res:
    print(j, end=' ')