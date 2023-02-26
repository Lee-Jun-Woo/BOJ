res = n = int(input())
if n != 1:
    while not (res % 2):
        print(2)
        res //= 2
    for i in range(3, n+2, 2):
        while not (res % i):
            print(i)
            res //= i