import sys
import heapq

input = sys.stdin.readline

arr = []
for _ in range(int(input())):
    h, o = map(int, input().split())
    if h > o:
        h, o = o, h
    arr.append((h, o))
l = int(input())
arr.sort(key=lambda x: x[1])

q = []
res = 0
cur = 0
rail = 0
for i in arr:
    heapq.heappush(q, i)
    cur += 1
    rail = i[1] - l
    while q and q[0][0] < rail:
        heapq.heappop(q)
        cur -= 1
    res = max(res, cur)

print(res)
