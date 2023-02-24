from sys import stdin

def is_prime(num: int) -> bool:
    if num < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n == 4: print('2 2')
    else:
        small = n // 2 - (n // 2 + 1) % 2
        while small >= 3:
            if is_prime(small) and is_prime(n-small):
                print(small, n-small)
                break
            small -= 2
        if small == 1: print(2, n-2)