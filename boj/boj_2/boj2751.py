import sys
values = []
for i in range(int(sys.stdin.readline())):
    values.append(int(sys.stdin.readline()))
values.sort()
for sorted_value in values:
    print(sorted_value)