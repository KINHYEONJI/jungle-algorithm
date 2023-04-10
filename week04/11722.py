import sys

input = sys.stdin.readline

n = int(input().rstrip())
numbers = list(map(int, input().rstrip().split()))

dp = [0 for _ in range(n)]
for i in range(n):
    dp[i] = 1
    for j in range(0, i):

        if numbers[j] > numbers[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))
