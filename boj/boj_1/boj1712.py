a, b, c = [int(num) for num in input().split()]
if b == c: print(-1)
elif int(a/(c-b)+1) > 0: print(int(a/(c-b)+1))
else: print(-1)