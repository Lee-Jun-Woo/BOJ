import sys
input = sys.stdin.readline

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def convex_hull(points):
    points = sorted(set(points))

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]

n, l = map(int, input().split())
pts = [tuple(map(int, input().split())) for _ in range(n)]
ch = convex_hull(pts)
res = 0.0

for i in range(len(ch) - 1):
    x1, y1 = ch[i]
    x2, y2 = ch[i + 1]
    res += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
x1, y1 = ch[-1]
x2, y2 = ch[0]
res += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(round(res + 2 * 3.14159265358979 * l))
