import sys

input = sys.stdin.readline

n = int(input().rstrip())
numbers = list(map(int, input().rstrip().split()))

decrease_dp = [1 for _ in range(n)]
increase_dp = [0 for _ in range(n)]

for i in range(n):
    for j in range(0, i):
        if numbers[i] > numbers[j]:
            increase_dp[i] = max(increase_dp[i], increase_dp[j] + 1)

for i in range(n - 1, -1, -1):
    for j in range(n - 1, i - 1, -1):
        if numbers[i] > numbers[j]:
            decrease_dp[i] = max(decrease_dp[i], decrease_dp[j] + 1)

max_ = 0
for i in range(n):
    max_ = max(max_, decrease_dp[i] + increase_dp[i])

print(max_)
