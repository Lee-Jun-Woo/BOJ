n, m = map(int, input().split())
str_set = dict()
for _ in range(n):
    str_set[input()] = 0
for _ in range(m):
    try:
        str_set[input()] += 1
    except KeyError:
        pass
print(sum(str_set.values()))