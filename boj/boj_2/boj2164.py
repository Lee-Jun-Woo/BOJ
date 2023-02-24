n = int(input())
exp = 2
while True:
    if n <= 2:
        print(n)
        break
    exp *= 2
    if exp >= n:
        print((n-exp//2)*2)
        break