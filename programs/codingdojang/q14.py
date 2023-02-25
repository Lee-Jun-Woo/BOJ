arr = input().split()
turn = int(arr[0])
arr = arr[1:]
arr = arr[-turn:] + arr[:-turn]
for data in arr: print(data, end=' ')