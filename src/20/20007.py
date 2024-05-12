import sys
import heapq

input = sys.stdin.readline

n, m, x, y = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

dist = [10**12] * n
dist[y] = 0
q = [(0, y)]

while q:
    d, v = heapq.heappop(q)
    if dist[v] < d:
        continue
    else:
        for z in graph[v]:
            nd = d + z[0]
            if nd < dist[z[1]]:
                dist[z[1]] = nd
                heapq.heappush(q, (nd, z[1]))

dist.sort()
res = 0
cur = 0
for i in dist:
    if 2 * i > x:
        print(-1)
        sys.exit()
    elif cur + 2 * i > x:
        res += 1
        cur = 2 * i
    else:
        cur += 2 * i
print(res + 1)
