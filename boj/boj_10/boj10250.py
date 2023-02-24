import math
for _ in range(int(input())):
    h, w, n = tuple(map(int, input().split()))
    floor = n % h
    if not floor: floor = h
    room = math.ceil(n / h)
    print('%d%02d' % (floor, room))