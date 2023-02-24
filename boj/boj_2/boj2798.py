n, m = map(int, input().split())
cards = tuple(map(int, input().split()))
max_sum = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            current_sum = cards[i] + cards[j] + cards[k]
            if max_sum < current_sum <= m:
                max_sum = current_sum

print(max_sum)