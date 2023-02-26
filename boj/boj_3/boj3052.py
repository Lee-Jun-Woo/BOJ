import sys
arr = []
for i in range(10):
    arr.append(int(sys.stdin.readline().rstrip()) % 42)
print(len(set(arr)))