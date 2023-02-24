a, b, c = [int(num) for num in input().split()]
nums = set((a, b, c))
if len(nums) == 1: print(10000 + a * 1000)
elif len(nums) == 2:
    if a == b: print(1000 + a * 100)
    else: print(1000 + c * 100)
else: print(max(nums) * 100)