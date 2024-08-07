import sys
import heapq

input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(v):
    a, *l = map(int, input().split())
    for i in range(len(l) // 2):
        graph[a].append((l[2 * i + 1], l[2 * i]))


def dijkstra(k: int) -> list[int]:
    res = [10**9] * (v + 1)
    res[0], res[k] = -1, 0
    q = [(0, k)]

    while q:
        d, x = heapq.heappop(q)
        if res[x] >= d:
            for nx in graph[x]:
                nd = d + nx[0]
                if nd < res[nx[1]]:
                    res[nx[1]] = nd
                    heapq.heappush(q, (nd, nx[1]))

    return res


first = dijkstra(1)
second, val = 0, 0
for i in range(1, v + 1):
    if first[i] > val:
        second, val = i, first[i]
print(max(dijkstra(second)))
