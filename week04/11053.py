import sys

input = sys.stdin.readline

n = int(input().rstrip())

numbers = list(map(int, input().rstrip().split()))

dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
