n = int(input())
nums = map(int, input().split())
res = 0
for i in nums:
    if i == 1: continue
    max = int(i ** 0.5) + 1
    for j in range(2, max):
        if not (i % j): break
    else:
        res += 1
print(res)