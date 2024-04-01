import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m, k = map(int, input().split())
arr = (0,) + tuple(map(int, input().split()))
parent = [i for i in range(n + 1)]
least = [10 ** 9 for _ in range(n + 1)]
res = 0

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

for i in range(n + 1):
    parent[i] = find(i)
    if arr[i] < least[parent[i]]:
        least[parent[i]] = arr[i]

for i in least:
    if i < 10 ** 9:
        res += i

print(res if res <= k else 'Oh no')
