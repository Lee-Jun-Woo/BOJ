nums = []
for _ in range(9):
    nums += input().split()
nums = list(map(int, nums))
largest_index = nums.index(max(nums))
print(max(nums))
print(largest_index//9+1, largest_index%9+1)