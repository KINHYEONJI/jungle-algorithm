import sys

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())
    dp = [1 for _ in range(100)]
    dp[3] = 2
    dp[4] = 2
    for i in range(5, n):
        dp[i] = dp[i - 1] + dp[i - 5]

    print(dp[n - 1])
