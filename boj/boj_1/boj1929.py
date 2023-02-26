m, n = map(int, input().split())
nums = range(m, n+1)
for i in nums:
    if i == 1: continue
    max = int(i ** 0.5) + 1
    for j in range(2, max):
        if not (i % j): break
    else:
        print(i)