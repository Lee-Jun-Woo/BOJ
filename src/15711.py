import sys

input = sys.stdin.readline

isprime = [True] * 2000001
isprime[0] = False
isprime[1] = False
for i in range(2, 1415):
    if isprime[i]:
        j = i
        while i * j <= 2000000:
            isprime[i * j] = False
            j += 1
prime = tuple(filter(lambda x: isprime[x], range(2, 2000001)))

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a + b == 2:
        print("NO")
    elif (a + b) % 2 == 0:
        print("YES")
    else:
        p = a + b - 2
        if p <= 2000000:
            print("YES" if isprime[p] else "NO")
        else:
            for i in prime:
                if p % i == 0:
                    print("NO")
                    break
            else:
                print("YES")
