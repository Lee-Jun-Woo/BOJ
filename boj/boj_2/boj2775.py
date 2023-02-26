def resident(a: int, b: int) -> int:
    if a:
        res = 0
        for i in range(1, b+1):
            res += resident(a-1, i)
        return res
    return b

for _ in range(int(input())):
    k = int(input())
    n = int(input())
    print(resident(k, n))