import sys

input = sys.stdin.readline

n = int(input().rstrip())

numbers = list(map(int, input().rstrip().split()))

dp = [0 for _ in range(n)]

for i in range(0, n):
    dp[i] = numbers[i]
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + numbers[i])

print(max(dp))
