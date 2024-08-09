import sys

input = sys.stdin.readline

n = int(input())
city = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = max(
            dp[i - 1][j] + (dp[i - 1][j] % 3 == city[i - 1][j - 1]),
            dp[i][j - 1] + (dp[i][j - 1] % 3 == city[i - 1][j - 1]),
        )

print(dp[n][n])
