n = int(input())
yak_su = list(map(int, input().split()))
yak_su.sort()
print(yak_su[0] * yak_su[-1])