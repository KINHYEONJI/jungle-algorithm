import sys

input = sys.stdin.readline

n = int(input().rstrip())
times = list(map(int, input().rstrip().split()))

times.sort()
dp = [0 for _ in range(n)]
dp[0] = times[0]
for i in range(1, n):
    dp[i] = dp[i - 1] + times[i]

print(sum(dp))
