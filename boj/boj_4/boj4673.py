def d(n: int) -> int:
    str_n = str(n)
    return n + sum([int(digit) for digit in str_n])

num_set = set()
for i in range(1, 10001): num_set.add(d(i))
for j in sorted(set(range(1, 10001)) - num_set): print(j)