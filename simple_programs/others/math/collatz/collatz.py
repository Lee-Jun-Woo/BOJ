# 콜라츠 수열 구현

def collatz(n: int) -> list:
    res = [n]
    while n != 1:
        if n % 2:
            n = 3 * n + 1
        else:
            n //= 2
        res.append(n)
    return res

if __name__ == '__main__':
    num = int(input())
    print(collatz(num))