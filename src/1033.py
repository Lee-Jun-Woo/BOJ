import sys
from collections import deque
from math import gcd
input = sys.stdin.readline

n = int(input())
tree = [[(0, 0)] * n for _ in range(n)]
for _ in range(n - 1):
    a, b, p, q = map(int, input().split())
    tree[a][b] = (p, q)
    tree[b][a] = (q, p)
amount = [(0, 0)] * n
amount[0] = (1, 1)
queue = deque([0])

while queue:
    x = queue.popleft()
    for i in range(n):
        if tree[i][x] != (0, 0) and amount[i] == (0, 0):
            amount[i] = (tree[i][x][0] * amount[x][0], tree[i][x][1] * amount[x][1])
            queue.append(i)

pro = 1
for i in range(n):
    pro *= amount[i][1]
amount_int = [amount[i][0] * pro // amount[i][1] for i in range(n)]
g = gcd(*amount_int)
for i in amount_int:
    print(i // g, end=' ')
