import sys
from collections import deque

input = sys.stdin.readline
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

r, c = map(int, input().split())
forest = [input().rstrip() for _ in range(r)]

water = deque()
hedge = deque()
wdist = [[10**9] * c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if forest[i][j] == "*":
            water.append((i, j))
            wdist[i][j] = 0
        if forest[i][j] == "S":
            hedge.append((i, j, 0))

while water:
    x, y = water.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (
            0 <= nx < r
            and 0 <= ny < c
            and forest[nx][ny] not in "*DX"
            and wdist[nx][ny] == 10**9
        ):
            wdist[nx][ny] = wdist[x][y] + 1
            water.append((nx, ny))

while hedge:
    x, y, t = hedge.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if forest[nx][ny] == "D":
                print(t + 1)
                exit()
            if forest[nx][ny] not in "*SX" and wdist[nx][ny] > t + 1:
                wdist[nx][ny] = -1
                hedge.append((nx, ny, t + 1))

print("KAKTUS")
