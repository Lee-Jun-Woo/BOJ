n = int(input())
one_to_m = 1
m = 1
result = 0

while one_to_m <= n:
    if (n - one_to_m) % m == 0:
        result += 1
    m += 1
    one_to_m += m

print(result)