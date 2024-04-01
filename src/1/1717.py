import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

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

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    r, a, b = map(int, input().split())
    if r:
        print('YES' if find(a) == find(b) else 'NO')
    else:
        union(a, b)
