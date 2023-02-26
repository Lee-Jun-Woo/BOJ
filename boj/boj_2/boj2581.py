m = int(input())
n = int(input())
nums = []
for i in range(m, n+1):
    if i == 1: continue
    max = int(i ** 0.5) + 1
    for j in range(2, max):
        if not (i % j): break
    else:
        nums.append(i)
if len(nums):
    print(sum(nums))
    print(min(nums))
else:
    print(-1)