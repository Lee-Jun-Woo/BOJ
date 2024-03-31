import sys
input = sys.stdin.readline

def ccw(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points):
    points = sorted(set(points))

    lower = []
    for p in points:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) < 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in points[::-1]:
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) < 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]

n = int(input())
pts = []
for _ in range(n):
    x, y, c = input().split()
    if c == 'Y':
        pts.append((int(x), int(y)))

res = convex_hull(pts)
print(len(res))
for i in res:
    print(*i)
