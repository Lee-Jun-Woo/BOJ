h, m = [int(time) for time in input().split()]
m -= 45
if m < 0:
    h -= 1
    m += 60
if h < 0:
    h += 24
print(h, m)