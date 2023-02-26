import sys
def bin_search(lst: list, data: int) -> int:
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if data == lst[mid]:
            return 1
        elif data > lst[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
m = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
for i in nums:
    print(bin_search(a, i))