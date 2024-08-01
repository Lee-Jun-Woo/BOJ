import sys

input = sys.stdin.readline

b = 1


def change(index):
    index += b
    while index > 0:
        tree[index] += 1
        index //= 2


def add(left, right):
    if left > right:
        return 0
    r = 0
    left += b
    right += b
    while left <= right:
        if left % 2 == 1:
            r += tree[left]
        if right % 2 == 0:
            r += tree[right]
        left = (left + 1) // 2
        right = (right - 1) // 2

    return r


n = int(input())
while b < n:
    b *= 2

p = tuple(map(int, input().split()))
arr = sorted(range(n), key=lambda x: p[x])
tree = [0] * (4 * n)
res = 0

for i in range(n):
    res += add(arr[i] + 1, n - 1)
    change(arr[i])

print(res)
