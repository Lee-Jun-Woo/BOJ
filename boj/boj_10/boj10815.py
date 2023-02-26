def bin_search(array, wanted):
    first, last = 0, len(array) - 1
    while first <= last:
        mid = (first + last) // 2
        if array[mid] == wanted:
            return 1
        if array[mid] > wanted:
            last = mid - 1
        else:
            first = mid + 1
    return 0

n = int(input())
cards = sorted(map(int, input().split()))
m = int(input())
checks = map(int, input().split())

for check in checks:
    print(bin_search(cards, check), end=' ')