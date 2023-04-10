import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]

for i in range(1, k + 1):
    for j in range(n + 1):
        if j == 0:
            dp[i][j] = 1
            continue

        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(dp[k][n] % 1000000000)
