import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
dp = [0 for _ in range(1001)]
dp[0] = 1

for i in range(1, k + 1):
    dp[i] = dp[i - 1] * (n + 1 - i) // i

print(dp[k] % 10007)
