a, b = [int(time) for time in input().split()]
c = int(input())
b += c
a += (b // 60)
b = b % 60
a = a % 24
print(a, b)